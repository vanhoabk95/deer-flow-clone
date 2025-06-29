# Copyright (c) 2025 Bytedance Ltd. and/or its affiliates
# SPDX-License-Identifier: MIT

import base64
import json
import logging
import os
from datetime import datetime
from typing import Annotated, List, Optional, cast
from uuid import uuid4

from pydantic import BaseModel

from fastapi import FastAPI, HTTPException, Query, File, Form, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response, StreamingResponse
from langchain_core.messages import AIMessageChunk, ToolMessage, BaseMessage
from langgraph.types import Command

from src.config.report_style import ReportStyle
from src.graph.builder import build_graph_with_memory
from src.prose.graph.builder import build_graph as build_prose_graph
from src.rag.retriever import Resource
from src.server.chat_request import (
    ChatRequest,
    GenerateProseRequest,
)
from src.server.config_request import ConfigResponse
from src.llms.llm import get_configured_llm_models

logger = logging.getLogger(__name__)

INTERNAL_SERVER_ERROR_DETAIL = "Internal Server Error"

app = FastAPI(
    title="DeerFlow API",
    description="API for Deer",
    version="0.1.0",
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

graph = build_graph_with_memory()


@app.post("/api/chat/stream")
async def chat_stream(request: ChatRequest):
    thread_id = request.thread_id
    if thread_id == "__default__":
        thread_id = str(uuid4())
    return StreamingResponse(
        _astream_workflow_generator(
            request.model_dump()["messages"],
            thread_id,
            request.resources,
            request.max_plan_iterations,
            request.max_step_num,
            request.max_search_results,
            request.auto_accepted_plan,
            request.interrupt_feedback,
            request.report_style,
        ),
        media_type="text/event-stream",
    )


async def _astream_workflow_generator(
    messages: List[dict],
    thread_id: str,
    resources: List[Resource],
    max_plan_iterations: int,
    max_step_num: int,
    max_search_results: int,
    auto_accepted_plan: bool,
    interrupt_feedback: str,
    report_style: ReportStyle,
):
    input_ = {
        "messages": messages,
        "plan_iterations": 0,
        "final_report": "",
        "current_plan": None,
        "observations": [],
        "auto_accepted_plan": auto_accepted_plan,
        "research_topic": messages[-1]["content"] if messages else "",
    }
    if not auto_accepted_plan and interrupt_feedback:
        resume_msg = f"[{interrupt_feedback}]"
        # add the last message to the resume message
        if messages:
            resume_msg += f" {messages[-1]['content']}"
        input_ = Command(resume=resume_msg)
    async for agent, _, event_data in graph.astream(
        input_,
        config={
            "thread_id": thread_id,
            "resources": resources,
            "max_plan_iterations": max_plan_iterations,
            "max_step_num": max_step_num,
            "max_search_results": max_search_results,
            "report_style": report_style.value,
        },
        stream_mode=["messages", "updates"],
        subgraphs=True,
    ):
        if isinstance(event_data, dict):
            if "__interrupt__" in event_data:
                yield _make_event(
                    "interrupt",
                    {
                        "thread_id": thread_id,
                        "id": event_data["__interrupt__"][0].ns[0],
                        "role": "assistant",
                        "content": event_data["__interrupt__"][0].value,
                        "finish_reason": "interrupt",
                        "options": [
                            {"text": "Edit plan", "value": "edit_plan"},
                            {"text": "Start research", "value": "accepted"},
                        ],
                    },
                )
            continue
        message_chunk, message_metadata = cast(
            tuple[BaseMessage, dict[str, any]], event_data
        )
        event_stream_message: dict[str, any] = {
            "thread_id": thread_id,
            "agent": agent[0].split(":")[0],
            "id": message_chunk.id,
            "role": "assistant",
            "content": message_chunk.content,
        }
        if message_chunk.additional_kwargs.get("reasoning_content"):
            event_stream_message["reasoning_content"] = message_chunk.additional_kwargs[
                "reasoning_content"
            ]
        if message_chunk.response_metadata.get("finish_reason"):
            event_stream_message["finish_reason"] = message_chunk.response_metadata.get(
                "finish_reason"
            )
        if isinstance(message_chunk, ToolMessage):
            # Tool Message - Return the result of the tool call
            event_stream_message["tool_call_id"] = message_chunk.tool_call_id
            yield _make_event("tool_call_result", event_stream_message)
        elif isinstance(message_chunk, AIMessageChunk):
            # AI Message - Raw message tokens
            if message_chunk.tool_calls:
                # AI Message - Tool Call
                event_stream_message["tool_calls"] = message_chunk.tool_calls
                event_stream_message["tool_call_chunks"] = (
                    message_chunk.tool_call_chunks
                )
                yield _make_event("tool_calls", event_stream_message)
            elif message_chunk.tool_call_chunks:
                # AI Message - Tool Call Chunks
                event_stream_message["tool_call_chunks"] = (
                    message_chunk.tool_call_chunks
                )
                yield _make_event("tool_call_chunks", event_stream_message)
            else:
                # AI Message - Raw message tokens
                yield _make_event("message_chunk", event_stream_message)


def _make_event(event_type: str, data: dict[str, any]):
    if data.get("content") == "":
        data.pop("content")
    return f"event: {event_type}\ndata: {json.dumps(data, ensure_ascii=False)}\n\n"

@app.post("/api/prose/generate")
async def generate_prose(request: GenerateProseRequest):
    try:
        sanitized_prompt = request.prompt.replace("\r\n", "").replace("\n", "")
        logger.info(f"Generating prose for prompt: {sanitized_prompt}")
        workflow = build_prose_graph()
        events = workflow.astream(
            {
                "content": request.prompt,
                "option": request.option,
                "command": request.command,
            },
            stream_mode="messages",
            subgraphs=True,
        )
        return StreamingResponse(
            (f"data: {event[0].content}\n\n" async for _, event in events),
            media_type="text/event-stream",
        )
    except Exception as e:
        logger.exception(f"Error occurred during prose generation: {str(e)}")
        raise HTTPException(status_code=500, detail=INTERNAL_SERVER_ERROR_DETAIL)


@app.get("/api/config", response_model=ConfigResponse)
async def config():
    """Get the config of the server."""
    return ConfigResponse(
        models=get_configured_llm_models(),
    )


# ============================================================================
# Knowledge Base Endpoints (Using LocalKnowledgeBaseProvider)
# ============================================================================

from src.knowledge_base import LocalKnowledgeBaseProvider

# Initialize knowledge base provider
kb_provider = LocalKnowledgeBaseProvider()

class KnowledgeBase(BaseModel):
    id: str
    name: str
    description: str = ""
    created_at: str
    updated_at: str
    document_count: int = 0

class Document(BaseModel):
    id: str
    knowledge_base_id: str
    name: str
    file_name: str
    file_type: str
    file_size: int
    status: str = "ready"  # pending, processing, ready, error
    error_message: str = ""
    created_at: str
    updated_at: str
    processing_started_at: Optional[str] = None
    processing_completed_at: Optional[str] = None

class CreateKnowledgeBaseRequest(BaseModel):
    name: str
    description: str = ""

@app.get("/api/knowledge-bases")
async def list_knowledge_bases():
    """Get all knowledge bases."""
    try:
        kbs = kb_provider.get_knowledge_bases()
        return [KnowledgeBase(**kb) for kb in kbs]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error listing knowledge bases: {str(e)}")

@app.post("/api/knowledge-bases")
async def create_knowledge_base(request: CreateKnowledgeBaseRequest):
    """Create a new knowledge base."""
    try:
        kb_id = kb_provider.create_knowledge_base(request.name, request.description)
        
        # Get the created KB metadata
        kbs = kb_provider.get_knowledge_bases()
        for kb in kbs:
            if kb["id"] == kb_id:
                return KnowledgeBase(**kb)
        
        raise HTTPException(status_code=500, detail="Knowledge base created but not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error creating knowledge base: {str(e)}")

@app.put("/api/knowledge-bases/{kb_id}")
async def update_knowledge_base(kb_id: str, request: CreateKnowledgeBaseRequest):
    """Update a knowledge base."""
    # For now, just return not implemented
    # TODO: Implement update functionality in LocalKnowledgeBaseProvider
    raise HTTPException(status_code=501, detail="Update knowledge base not implemented yet")

@app.delete("/api/knowledge-bases/{kb_id}")
async def delete_knowledge_base(kb_id: str):
    """Delete a knowledge base."""
    try:
        success = kb_provider.delete_knowledge_base(kb_id)
        if success:
            return {"message": "Knowledge base deleted successfully"}
        else:
            raise HTTPException(status_code=404, detail="Knowledge base not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error deleting knowledge base: {str(e)}")

@app.get("/api/knowledge-bases/search")
async def search_knowledge_bases(query: str = ""):
    """Search knowledge bases by name or description."""
    try:
        resources = kb_provider.list_resources(query if query else None)
        kbs = []
        for resource in resources:
            kb_id = resource.uri.replace("kb://", "")
            kbs.append({
                "id": kb_id,
                "name": resource.title,
                "description": resource.description,
                "created_at": datetime.now().isoformat(),
                "updated_at": datetime.now().isoformat(),
                "document_count": 0
            })
        return [KnowledgeBase(**kb) for kb in kbs]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error searching knowledge bases: {str(e)}")

@app.get("/api/knowledge-bases/{kb_id}/documents")
async def list_documents(kb_id: str):
    """Get all documents in a knowledge base."""
    try:
        # Get documents from knowledge base
        documents = kb_provider.get_documents(kb_id)
        return [Document(**doc) for doc in documents]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error listing documents: {str(e)}")

@app.post("/api/knowledge-bases/{kb_id}/documents")
async def upload_document(
    kb_id: str,
    file: UploadFile = File(...),
    knowledge_base_id: str = Form(...)
):
    """Upload a document to a knowledge base."""
    try:
        # Check if knowledge base exists
        kbs = kb_provider.get_knowledge_bases()
        if not any(kb["id"] == kb_id for kb in kbs):
            raise HTTPException(status_code=404, detail="Knowledge base not found")
        
        # Save uploaded file
        kb_path = os.path.join(kb_provider.appdata_path, kb_id)
        docs_path = os.path.join(kb_path, "documents")
        
        if not os.path.exists(docs_path):
            os.makedirs(docs_path, exist_ok=True)
        
        file_path = os.path.join(docs_path, file.filename)
        
        # Check if file already exists
        if os.path.exists(file_path):
            raise HTTPException(
                status_code=409, 
                detail=f"Tài liệu '{file.filename}' đã tồn tại trong knowledge base này. Vui lòng đổi tên file hoặc xóa tài liệu cũ trước khi upload."
            )
        
        # Save file
        with open(file_path, "wb") as buffer:
            content = await file.read()
            buffer.write(content)
        
        # Add document metadata (this sets status to "pending")
        kb_provider.metadata_manager.add_document_metadata(kb_id, file.filename)
        
        # Process document in background (convert to markdown and index)
        import asyncio
        asyncio.create_task(kb_provider.process_document(kb_id, file.filename))
        
        # Get the created document metadata
        doc = kb_provider.get_document_status(kb_id, file.filename)
        if doc:
            return Document(**doc)
        
        raise HTTPException(status_code=500, detail="Document uploaded but metadata not found")
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error uploading document: {str(e)}")

@app.get("/api/knowledge-bases/{kb_id}/documents/{doc_id}")
async def get_document_status(kb_id: str, doc_id: str):
    """Get document status by document ID."""
    try:
        # Get all documents and find by doc_id
        documents = kb_provider.get_documents(kb_id)
        for doc in documents:
            if doc["id"] == doc_id:
                return Document(**doc)
        
        raise HTTPException(status_code=404, detail="Document not found")
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error getting document status: {str(e)}")

@app.delete("/api/knowledge-bases/{kb_id}/documents/{doc_id}")
async def delete_document(kb_id: str, doc_id: str):
    """Delete a document from a knowledge base."""
    try:
        # Get document by ID to find filename
        documents = kb_provider.get_documents(kb_id)
        target_doc = None
        for doc in documents:
            if doc["id"] == doc_id:
                target_doc = doc
                break
        
        if not target_doc:
            raise HTTPException(status_code=404, detail="Document not found")
        
        filename = target_doc["file_name"]
        
        # Delete document completely (files, metadata, and vectorstore)
        success = kb_provider.delete_document_complete(kb_id, filename)
        
        if success:
            return {"message": "Document deleted successfully from all locations"}
        else:
            return {"message": "Document deleted with some warnings - check server logs"}
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error deleting document: {str(e)}")
