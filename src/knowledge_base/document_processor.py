# Copyright (c) 2025 Bytedance Ltd. and/or its affiliates
# SPDX-License-Identifier: MIT

import os
import asyncio
from typing import List

from langchain_core.documents import Document as LCDocument


class DocumentProcessor:
    """Handles document processing: conversion to markdown and vectorization."""
    
    def __init__(self, appdata_path: str):
        self.appdata_path = appdata_path
    
    async def convert_to_markdown(self, file_path: str, filename: str) -> str:
        """Convert document to markdown based on file type."""
        file_ext = os.path.splitext(filename)[1].lower()
        
        if file_ext == '.pdf':
            import pymupdf4llm
            return pymupdf4llm.to_markdown(file_path)
        
        elif file_ext in ['.txt', '.md']:
            with open(file_path, 'r', encoding='utf-8') as f:
                return f.read()
        
        elif file_ext in ['.doc', '.docx']:
            return f"# {filename}\n\nWord document processing not implemented yet."
        
        else:
            return f"# {filename}\n\nUnsupported file type: {file_ext}"
    
    async def create_embeddings(self, embedding_model: str):
        """Create and test embeddings connection."""
        from langchain_ollama import OllamaEmbeddings
        
        try:
            embeddings = OllamaEmbeddings(model=embedding_model)
            # Test connection
            await embeddings.aembed_query("test connection")
            return embeddings
        except Exception as e:
            raise Exception(
                f"Failed to connect to Ollama. Please check that Ollama is downloaded, "
                f"running and accessible. https://ollama.com/download. Error: {str(e)}"
            )
    
    async def chunk_document(self, markdown_content: str, filename: str, kb_id: str, 
                           embeddings) -> List[LCDocument]:
        """Chunk document using semantic chunker."""
        from langchain_experimental.text_splitter import SemanticChunker
        
        # Create initial document
        initial_doc = LCDocument(
            page_content=markdown_content,
            metadata={
                "source": filename,
                "knowledge_base": kb_id,
                "file_type": os.path.splitext(filename)[1].lower(),
                "file_name": filename
            }
        )
        
        try:
            semantic_chunker = SemanticChunker(
                embeddings,
                breakpoint_threshold_type="percentile",
                breakpoint_threshold_amount=95,
            )
            
            chunks = semantic_chunker.split_documents([initial_doc])
            
            # Enhance chunks with metadata
            enhanced_chunks = []
            for chunk_idx, chunk in enumerate(chunks):
                enhanced_metadata = {
                    **chunk.metadata,
                    "chunk_index": chunk_idx,
                    "total_chunks": len(chunks),
                    "chunk_length": len(chunk.page_content),
                }
                
                enhanced_chunk = LCDocument(
                    page_content=chunk.page_content,
                    metadata=enhanced_metadata
                )
                enhanced_chunks.append(enhanced_chunk)
            
            return enhanced_chunks
            
        except Exception as e:
            raise Exception(
                f"Failed to chunk document using semantic chunker. "
                f"This usually indicates an Ollama connection issue. Error: {str(e)}"
            )
    
    async def index_to_vectorstore(self, chunks: List[LCDocument], lancedb_dir: str, 
                                 embeddings) -> None:
        """Index chunks into LanceDB vector store."""
        import lancedb
        from langchain_community.vectorstores import LanceDB
        
        try:
            vectorstore = LanceDB(
                uri=lancedb_dir,
                embedding=embeddings,
                table_name="documents",
                mode="append"
            )
            
            await vectorstore.aadd_documents(chunks)
            
        except Exception as e:
            raise Exception(
                f"Failed to index document into vector database. "
                f"This may be due to Ollama connection issues during embedding generation. "
                f"Error: {str(e)}"
            )
    
    def delete_from_vectorstore(self, kb_id: str, filename: str) -> bool:
        """Delete document vectors from LanceDB vectorstore."""
        kb_path = os.path.join(self.appdata_path, kb_id)
        lancedb_path = os.path.join(kb_path, "lancedb")
        
        if not os.path.exists(lancedb_path):
            print(f"LanceDB path not found: {lancedb_path}")
            return False
        
        try:
            import lancedb
            
            db = lancedb.connect(lancedb_path)
            
            if "documents" not in db.table_names():
                print("Documents table not found in LanceDB")
                return False
            
            table = db.open_table("documents")
            deleted_count = table.delete(f"source = '{filename}'")
            
            print(f"Deleted {deleted_count} vector records for document: {filename}")
            return True
            
        except Exception as e:
            print(f"Error deleting document from vectorstore {kb_id}: {e}")
            return False 