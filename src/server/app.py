# Copyright (c) 2025 Bytedance Ltd. and/or its affiliates
# SPDX-License-Identifier: MIT

import base64
import json
import logging
import os
from typing import Annotated, List, cast
from uuid import uuid4

from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response, StreamingResponse
from langchain_core.messages import AIMessageChunk, ToolMessage, BaseMessage
from langgraph.types import Command

from src.config.report_style import ReportStyle
from src.config.tools import SELECTED_RAG_PROVIDER
from src.graph.builder import build_graph_with_memory
# from src.podcast.graph.builder import build_graph as build_podcast_graph  # Podcast removed
# from src.ppt.graph.builder import build_graph as build_ppt_graph  # PPT removed
from src.prose.graph.builder import build_graph as build_prose_graph
# from src.prompt_enhancer.graph.builder import build_graph as build_prompt_enhancer_graph  # Prompt enhancer removed
from src.rag.builder import build_retriever
from src.rag.retriever import Resource
from src.server.chat_request import (
    ChatRequest,
    # EnhancePromptRequest,  # Prompt enhancer removed
    # GeneratePodcastRequest,  # Podcast removed
    # GeneratePPTRequest,  # PPT removed
    GenerateProseRequest,
    # TTSRequest,  # TTS removed
)

from src.server.rag_request import (
    RAGConfigResponse,
    RAGResourceRequest,
    RAGResourcesResponse,
)
from src.server.config_request import ConfigResponse
from src.llms.llm import get_configured_llm_models
# from src.tools import VolcengineTTS  # TTS removed

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


@app.get("/api/rag/config", response_model=RAGConfigResponse)
async def rag_config():
    """Get the config of the RAG."""
    return RAGConfigResponse(provider=SELECTED_RAG_PROVIDER)


@app.get("/api/rag/resources", response_model=RAGResourcesResponse)
async def rag_resources(request: Annotated[RAGResourceRequest, Query()]):
    """Get the resources of the RAG."""
    retriever = build_retriever()
    if retriever:
        return RAGResourcesResponse(resources=retriever.list_resources(request.query))
    return RAGResourcesResponse(resources=[])


@app.get("/api/config", response_model=ConfigResponse)
async def config():
    """Get the config of the server."""
    return ConfigResponse(
        rag=RAGConfigResponse(provider=SELECTED_RAG_PROVIDER),
        models=get_configured_llm_models(),
    )


# ============================================================================
# Knowledge Base Endpoints (Simple in-memory implementation for demo)
# ============================================================================

# Simple in-memory storage for demo purposes
knowledge_bases = {}
documents = {}
document_counter = 0
kb_counter = 0

from datetime import datetime
from fastapi import UploadFile, File, Form
from pydantic import BaseModel

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
    status: str = "ready"  # uploading, indexing, ready, error
    error_message: str = ""
    created_at: str
    updated_at: str

class CreateKnowledgeBaseRequest(BaseModel):
    name: str
    description: str = ""

@app.get("/api/knowledge-bases")
async def list_knowledge_bases():
    """Get all knowledge bases."""
    return list(knowledge_bases.values())

@app.post("/api/knowledge-bases")
async def create_knowledge_base(request: CreateKnowledgeBaseRequest):
    """Create a new knowledge base."""
    global kb_counter
    kb_counter += 1
    kb_id = f"kb_{kb_counter}"
    now = datetime.now().isoformat()
    
    kb = KnowledgeBase(
        id=kb_id,
        name=request.name,
        description=request.description,
        created_at=now,
        updated_at=now,
        document_count=0
    )
    knowledge_bases[kb_id] = kb
    documents[kb_id] = []
    return kb

@app.put("/api/knowledge-bases/{kb_id}")
async def update_knowledge_base(kb_id: str, request: CreateKnowledgeBaseRequest):
    """Update a knowledge base."""
    if kb_id not in knowledge_bases:
        raise HTTPException(status_code=404, detail="Knowledge base not found")
    
    kb = knowledge_bases[kb_id]
    kb.name = request.name
    kb.description = request.description
    kb.updated_at = datetime.now().isoformat()
    return kb

@app.delete("/api/knowledge-bases/{kb_id}")
async def delete_knowledge_base(kb_id: str):
    """Delete a knowledge base."""
    if kb_id not in knowledge_bases:
        raise HTTPException(status_code=404, detail="Knowledge base not found")
    
    del knowledge_bases[kb_id]
    if kb_id in documents:
        del documents[kb_id]
    return {"message": "Knowledge base deleted successfully"}

@app.get("/api/knowledge-bases/search")
async def search_knowledge_bases(query: str = ""):
    """Search knowledge bases by name or description."""
    if not query:
        return list(knowledge_bases.values())
    
    query_lower = query.lower()
    result = []
    for kb in knowledge_bases.values():
        if (query_lower in kb.name.lower() or 
            query_lower in kb.description.lower()):
            result.append(kb)
    return result

@app.get("/api/knowledge-bases/{kb_id}/documents")
async def list_documents(kb_id: str):
    """Get all documents in a knowledge base."""
    if kb_id not in knowledge_bases:
        raise HTTPException(status_code=404, detail="Knowledge base not found")
    return documents.get(kb_id, [])

@app.post("/api/knowledge-bases/{kb_id}/documents")
async def upload_document(
    kb_id: str,
    file: UploadFile = File(...),
    knowledge_base_id: str = Form(...)
):
    """Upload a document to a knowledge base."""
    if kb_id not in knowledge_bases:
        raise HTTPException(status_code=404, detail="Knowledge base not found")
    
    global document_counter
    document_counter += 1
    doc_id = f"doc_{document_counter}"
    now = datetime.now().isoformat()
    
    # Read file content (for demo, we just store metadata)
    content = await file.read()
    
    doc = Document(
        id=doc_id,
        knowledge_base_id=kb_id,
        name=file.filename or f"Document {document_counter}",
        file_name=file.filename or f"document_{document_counter}",
        file_type=file.content_type or "application/octet-stream",
        file_size=len(content),
        status="ready",  # For demo, immediately mark as ready
        created_at=now,
        updated_at=now
    )
    
    if kb_id not in documents:
        documents[kb_id] = []
    documents[kb_id].append(doc)
    
    # Update document count
    knowledge_bases[kb_id].document_count = len(documents[kb_id])
    knowledge_bases[kb_id].updated_at = now
    
    return doc

@app.get("/api/knowledge-bases/{kb_id}/documents/{doc_id}")
async def get_document_status(kb_id: str, doc_id: str):
    """Get document status."""
    if kb_id not in knowledge_bases:
        raise HTTPException(status_code=404, detail="Knowledge base not found")
    
    kb_docs = documents.get(kb_id, [])
    for doc in kb_docs:
        if doc.id == doc_id:
            return doc
    
    raise HTTPException(status_code=404, detail="Document not found")

@app.delete("/api/knowledge-bases/{kb_id}/documents/{doc_id}")
async def delete_document(kb_id: str, doc_id: str):
    """Delete a document from a knowledge base."""
    if kb_id not in knowledge_bases:
        raise HTTPException(status_code=404, detail="Knowledge base not found")
    
    kb_docs = documents.get(kb_id, [])
    for i, doc in enumerate(kb_docs):
        if doc.id == doc_id:
            del kb_docs[i]
            # Update document count
            knowledge_bases[kb_id].document_count = len(kb_docs)
            knowledge_bases[kb_id].updated_at = datetime.now().isoformat()
            return {"message": "Document deleted successfully"}
    
    raise HTTPException(status_code=404, detail="Document not found")
