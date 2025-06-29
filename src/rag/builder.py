# Copyright (c) 2025 Bytedance Ltd. and/or its affiliates
# SPDX-License-Identifier: MIT

from src.rag.retriever import Retriever


def build_retriever() -> Retriever:
    """Build and return local knowledge base retriever."""
    from src.knowledge_base import LocalKnowledgeBaseProvider
    return LocalKnowledgeBaseProvider()
