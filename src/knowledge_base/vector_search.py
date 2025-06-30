# Copyright (c) 2025 Bytedance Ltd. and/or its affiliates
# SPDX-License-Identifier: MIT

import os
import hashlib
from typing import List

from src.rag.retriever import Chunk, Document


class VectorSearchManager:
    """Manages vector search operations."""
    
    def __init__(self, appdata_path: str, max_results: int = 10):
        self.appdata_path = appdata_path
        self.max_results = max_results
    
    def search_in_kb(self, kb_id: str, query: str) -> List[Document]:
        """Search documents in a specific knowledge base using LanceDB."""
        kb_path = os.path.join(self.appdata_path, kb_id)
        lancedb_path = os.path.join(kb_path, "lancedb")
        
        if not os.path.exists(lancedb_path):
            return []
        
        try:
            return self._perform_search(lancedb_path, query)
        except Exception as e:
            print(f"Error searching in knowledge base {kb_id}: {e}")
            return []
    
    def _perform_search(self, lancedb_path: str, query: str) -> List[Document]:
        """Perform the actual vector search."""
        import lancedb
        from langchain_community.vectorstores import LanceDB
        from langchain_ollama import OllamaEmbeddings
        
        # Initialize embeddings
        embeddings = OllamaEmbeddings(
            model=os.getenv("EMBEDDING_MODEL", "nomic-embed-text")
        )
        
        # Connect to LanceDB
        vectorstore = LanceDB(
            uri=lancedb_path,
            embedding=embeddings,
            table_name="documents"
        )
        
        # Perform search
        retriever = vectorstore.as_retriever(
            search_kwargs={"k": self.max_results}
        )
        
        # Get documents
        langchain_docs = retriever.invoke(query)
        
        # Convert to our Document format
        return self._convert_to_documents(langchain_docs)
    
    def _convert_to_documents(self, langchain_docs) -> List[Document]:
        """Convert LangChain documents to our Document format."""
        documents = []
        doc_groups = {}  # Group chunks by document
        
        for lc_doc in langchain_docs:
            metadata = lc_doc.metadata
            doc_id = metadata.get(
                "source", 
                f"doc_{hashlib.md5(lc_doc.page_content.encode()).hexdigest()[:8]}"
            )
            doc_title = metadata.get("title", doc_id)
            similarity = metadata.get("similarity", 0.8)
            
            if doc_id not in doc_groups:
                doc_groups[doc_id] = Document(
                    id=doc_id,
                    title=doc_title,
                    chunks=[],
                    metadata={
                        "file_type": metadata.get("file_type", ""),
                        "file_name": metadata.get("file_name", doc_title),
                        "file_path": metadata.get("file_path", ""),
                        "knowledge_base": metadata.get("knowledge_base", ""),
                    }
                )
            
            chunk = Chunk(
                content=lc_doc.page_content,
                similarity=similarity,
                metadata={
                    "page_number": metadata.get("page_number"),
                    "file_type": metadata.get("file_type", ""),
                    "chunk_index": metadata.get("chunk_index", 0),
                }
            )
            doc_groups[doc_id].chunks.append(chunk)
        
        return list(doc_groups.values()) 