# Copyright (c) 2025 Bytedance Ltd. and/or its affiliates
# SPDX-License-Identifier: MIT

import logging
from typing import List, Optional, Type
from langchain_core.tools import BaseTool
from langchain_core.callbacks import (
    AsyncCallbackManagerForToolRun,
    CallbackManagerForToolRun,
)
from pydantic import BaseModel, Field

from src.config.tools import SELECTED_RAG_PROVIDER
from src.rag.retriever import Document, Retriever, Resource
from src.rag.builder import build_retriever

logger = logging.getLogger(__name__)


class RetrieverInput(BaseModel):
    keywords: str = Field(description="search keywords to look up")


class RetrieverTool(BaseTool):
    name: str = "local_search_tool"
    description: str = (
        "Useful for retrieving information from local knowledge bases with `kb://` uri prefix, it should be higher priority than the web search or writing code. Input should be a search keywords."
    )
    args_schema: Type[BaseModel] = RetrieverInput

    retriever: Optional[Retriever] = Field(default=None)
    resources: List[Resource] = Field(default_factory=list)

    def _run(
        self,
        keywords: str,
        run_manager: Optional[CallbackManagerForToolRun] = None,
    ) -> str:
        logger.info(
            f"Retriever tool query: {keywords}", extra={"resources": self.resources}
        )
        if not self.retriever:
            return "No retriever available."
        
        documents = self.retriever.query_relevant_documents(keywords, self.resources)
        if not documents:
            return "No results found from the local knowledge base."
        
        # Format results as string for agent consumption
        result_lines = []
        for doc in documents:
            result_lines.append(f"Document: {doc.title}")
            for chunk in doc.chunks:
                result_lines.append(f"Content: {chunk.content}")
                result_lines.append(f"Similarity: {chunk.similarity}")
            result_lines.append("---")
        
        return "\n".join(result_lines)

    async def _arun(
        self,
        keywords: str,
        run_manager: Optional[AsyncCallbackManagerForToolRun] = None,
    ) -> str:
        return self._run(keywords, run_manager.get_sync() if run_manager else None)


def get_retriever_tool(resources: List[Resource]) -> Optional[RetrieverTool]:
    if not resources:
        return None
    logger.info(f"create retriever tool: {SELECTED_RAG_PROVIDER}")
    retriever = build_retriever()

    if not retriever:
        return None
    
    # Convert Resource objects to dict format for Pydantic
    resources_data = []
    for resource in resources:
        if hasattr(resource, 'model_dump'):
            resources_data.append(resource.model_dump())
        elif hasattr(resource, 'dict'):
            resources_data.append(resource.dict())
        else:
            # Manual conversion
            resources_data.append({
                'uri': resource.uri,
                'title': resource.title,
                'description': resource.description or ""
            })
    
    # Create tool with dict resources and then convert back
    tool = RetrieverTool()
    tool.retriever = retriever
    tool.resources = [Resource(**data) for data in resources_data]
    
    return tool
