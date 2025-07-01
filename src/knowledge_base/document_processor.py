# Copyright (c) 2025 Bytedance Ltd. and/or its affiliates
# SPDX-License-Identifier: MIT

import os
from typing import List

from dotenv import load_dotenv

from langchain_core.documents import Document as LCDocument
from langchain_community.vectorstores import LanceDB
from langchain.text_splitter import RecursiveCharacterTextSplitter
import lancedb
from langchain_ollama import OllamaEmbeddings

load_dotenv()

class DocumentProcessor:
    """Handles document processing: conversion to markdown and vectorization."""
    
    def __init__(self, appdata_path: str):
        self.appdata_path = appdata_path
    
    async def convert_to_markdown(self, file_path: str, filename: str) -> str | list:
        """Convert document to markdown based on file type."""
        file_ext = os.path.splitext(filename)[1].lower()
        
        if file_ext == '.pdf':
            import pymupdf4llm
            # Sử dụng page_chunks=True để lấy thông tin page
            return pymupdf4llm.to_markdown(file_path, page_chunks=True)
        
        elif file_ext in ['.txt', '.md']:
            with open(file_path, 'r', encoding='utf-8') as f:
                return f.read()
        
        elif file_ext in ['.doc', '.docx']:
            return f"# {filename}\n\nWord document processing not implemented yet."
        
        else:
            return f"# {filename}\n\nUnsupported file type: {file_ext}"
    
    async def create_embeddings(self, embedding_model: str):
        """Create and test embeddings connection."""
        
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
    
    async def chunk_document(self, markdown_content: str | list, filename: str, kb_id: str, 
                           embeddings, file_path: str = None) -> List[LCDocument]:
        """Chunk document using RecursiveCharacterTextSplitter with basic metadata."""
        
        file_ext = os.path.splitext(filename)[1].lower()
        
        # Handle PDF with page chunks
        if file_ext == '.pdf' and isinstance(markdown_content, list):
            return self._chunk_pdf_pages(markdown_content, filename, kb_id, file_path)
        
        # Handle other document types
        return self._chunk_text_document(markdown_content, filename, kb_id, file_path)
    
    def _chunk_pdf_pages(self, page_data: list, filename: str, kb_id: str, 
                        file_path: str) -> List[LCDocument]:
        """Chunk PDF pages with simplified metadata."""
        
        all_chunks = []
        
        # Tạo text splitter - đọc cấu hình từ environment variables
        chunk_size = int(os.getenv("CHUNK_SIZE", "2500"))
        chunk_overlap = int(os.getenv("CHUNK_OVERLAP", "500"))
        
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            length_function=len,
        )
        
        for page_info in page_data:
            page_text = page_info.get('text', '')
            page_metadata = page_info.get('metadata', {})
            page_number = page_metadata.get('page', 1)
            
            if not page_text.strip():
                continue
            
            # Create basic metadata for page
            page_doc = LCDocument(
                page_content=page_text,
                metadata={
                    "source": filename,
                    "knowledge_base": kb_id,
                    "file_type": ".pdf",
                    "file_name": filename,
                    "file_path": file_path or "",
                    "page_number": page_number,
                }
            )
            
            # Chunk this page
            try:
                page_chunks = text_splitter.split_documents([page_doc])
                
                # Add chunk metadata
                for chunk_idx, chunk in enumerate(page_chunks):
                    chunk.metadata.update({
                        "chunk_index": len(all_chunks),
                        "page_chunk_index": chunk_idx,
                    })
                    all_chunks.append(chunk)
                        
            except Exception:
                # Fallback: treat page as single chunk
                page_doc.metadata["chunk_index"] = len(all_chunks)
                all_chunks.append(page_doc)
        
        return all_chunks
    
    def _chunk_text_document(self, markdown_content: str | list, filename: str, kb_id: str,
                           file_path: str) -> List[LCDocument]:
        """Chunk non-PDF documents with basic metadata."""
        
        # Convert list to string if needed
        if isinstance(markdown_content, list):
            markdown_content = str(markdown_content)
        
        file_ext = os.path.splitext(filename)[1].lower()
        
        initial_doc = LCDocument(
            page_content=markdown_content,
            metadata={
                "source": filename,
                "knowledge_base": kb_id,
                "file_type": file_ext,
                "file_name": filename,
                "file_path": file_path or "",
            }
        )
        
        try:
            # Tạo text splitter - đọc cấu hình từ environment variables
            chunk_size = int(os.getenv("CHUNK_SIZE", "2500"))
            chunk_overlap = int(os.getenv("CHUNK_OVERLAP", "500"))
            
            text_splitter = RecursiveCharacterTextSplitter(
                chunk_size=chunk_size,
                chunk_overlap=chunk_overlap,
                length_function=len,
            )
            
            chunks = text_splitter.split_documents([initial_doc])
            
            # Add basic chunk metadata
            for chunk_idx, chunk in enumerate(chunks):
                chunk.metadata["chunk_index"] = chunk_idx
            
            return chunks
            
        except Exception as e:
            raise Exception(
                f"Failed to chunk document using RecursiveCharacterTextSplitter. Error: {str(e)}"
            )
    
    async def index_to_vectorstore(self, chunks: List[LCDocument], lancedb_dir: str, 
                                 embeddings) -> None:
        """Index chunks into LanceDB vector store.""" 
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
                f"Failed to index document into vector database. Error: {str(e)}"
            )
    
    def delete_from_vectorstore(self, kb_id: str, filename: str) -> bool:
        """Delete document vectors from LanceDB vectorstore."""
        kb_path = os.path.join(self.appdata_path, kb_id)
        lancedb_path = os.path.join(kb_path, "lancedb")
        
        if not os.path.exists(lancedb_path):
            print(f"LanceDB path not found: {lancedb_path}")
            return False
        
        try:
            db = lancedb.connect(lancedb_path)
            
            if "documents" not in db.table_names():
                print("Documents table not found in LanceDB")
                return False
            
            table = db.open_table("documents")
            deleted_count = table.delete(f"metadata.source = '{filename}'")
            
            print(f"Deleted {deleted_count} vector records for document: {filename}")
            return True
            
        except Exception as e:
            print(f"Error deleting document from vectorstore {kb_id}: {e}")
            return False 