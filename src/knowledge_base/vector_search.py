# Copyright (c) 2025 Bytedance Ltd. and/or its affiliates
# SPDX-License-Identifier: MIT

import os
import hashlib
from typing import List

import lancedb
from langchain_community.vectorstores import LanceDB
from langchain_ollama import OllamaEmbeddings

from dotenv import load_dotenv

from src.rag.retriever import Chunk, Document

load_dotenv()

class VectorSearchManager:
    """Manages vector search operations with hybrid search support."""
    
    def __init__(self, appdata_path: str, max_results: int = 10):
        self.appdata_path = appdata_path
        self.max_results = max_results
    
    def search_in_kb(self, kb_id: str, query: str, use_hybrid: bool = False) -> List[Document]:
        """Search documents in a specific knowledge base using LanceDB.
        
        Args:
            kb_id: Knowledge base identifier
            query: Search query string
            use_hybrid: Whether to use hybrid search (combines vector + full-text search)
        """
        kb_path = os.path.join(self.appdata_path, kb_id)
        lancedb_path = os.path.join(kb_path, "lancedb")
        
        if not os.path.exists(lancedb_path):
            return []
        
        try:
            return self._perform_search(lancedb_path, query, use_hybrid)
        except Exception as e:
            print(f"Error searching in knowledge base {kb_id}: {e}")
            return []
    
    def _perform_search(self, lancedb_path: str, query: str, use_hybrid: bool = False) -> List[Document]:
        """Perform the actual vector search with optional hybrid search."""
        # Initialize embeddings
        embeddings = OllamaEmbeddings(
            model=os.getenv("EMBEDDING_MODEL", "nomic-embed-text:latest")
        )
        
        # Connect to LanceDB
        vectorstore = LanceDB(
            uri=lancedb_path,
            embedding=embeddings,
            table_name="documents"
        )
        
        if use_hybrid:
            # Sử dụng hybrid search - kết hợp vector search và full-text search
            # LanceDB tự động merge kết quả từ cả hai phương pháp
            try:
                # Kiểm tra xem có FTS index không, nếu không thì tạo
                db = lancedb.connect(lancedb_path)
                table = db.open_table("documents")
                
                # Tạo FTS index nếu chưa có (chỉ cần làm một lần)
                try:
                    # Thử search để kiểm tra index có tồn tại không
                    table.search(query, query_type="fts").limit(1).to_pandas()
                except Exception:
                    # Nếu lỗi thì tạo FTS index
                    print("Creating FTS index for hybrid search...")
                    table.create_fts_index("text", replace=True)
                
                # Thực hiện hybrid search
                results = table.search(query, query_type="hybrid").limit(self.max_results).to_pandas()
                
                # Convert pandas DataFrame thành LangChain documents
                langchain_docs = []
                for _, row in results.iterrows():
                    from langchain_core.documents import Document as LCDocument
                    doc = LCDocument(
                        page_content=row.get('text', ''),
                        metadata=row.to_dict()
                    )
                    langchain_docs.append(doc)
                    
            except Exception as e:
                print(f"Hybrid search failed, falling back to vector search: {e}")
                # Fallback về vector search thông thường
                retriever = vectorstore.as_retriever(
                    search_kwargs={"k": self.max_results}
                )
                langchain_docs = retriever.invoke(query)
        else:
            # Vector search thông thường
            retriever = vectorstore.as_retriever(
                search_kwargs={"k": self.max_results}
            )
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