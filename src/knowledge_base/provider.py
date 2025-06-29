# Copyright (c) 2025 Bytedance Ltd. and/or its affiliates
# SPDX-License-Identifier: MIT

import os
import shutil
import asyncio
import traceback
from datetime import datetime
from typing import List, Dict, Any, Optional

from src.rag.retriever import Retriever, Resource, Document
from .metadata import MetadataManager
from .document_processor import DocumentProcessor
from .vector_search import VectorSearchManager
from .utils import parse_kb_uri, setup_kb_directories


class LocalKnowledgeBaseProvider(Retriever):
    """
    LocalKnowledgeBaseProvider uses local LanceDB and file system 
    for knowledge base management.
    """

    def __init__(self):
        self.appdata_path = os.path.join(os.getcwd(), "appdata")
        if not os.path.exists(self.appdata_path):
            os.makedirs(self.appdata_path)
        
        self.max_results = int(os.getenv("LOCAL_KB_MAX_RESULTS", "10"))
        
        # Initialize managers
        self.metadata_manager = MetadataManager(self.appdata_path)
        self.document_processor = DocumentProcessor(self.appdata_path)
        self.vector_search_manager = VectorSearchManager(self.appdata_path, self.max_results)

    def list_resources(self, query: str | None = None) -> List[Resource]:
        """List all knowledge bases as resources."""
        resources = []
        
        for kb_dir in os.listdir(self.appdata_path):
            kb_path = os.path.join(self.appdata_path, kb_dir)
            if not os.path.isdir(kb_path):
                continue
                
            # Check if this is a valid knowledge base
            lancedb_path = os.path.join(kb_path, "lancedb")
            if not os.path.exists(lancedb_path):
                continue
                
            metadata = self.metadata_manager.get_kb_metadata(kb_path)
            
            # Filter by query if provided
            if query:
                query_lower = query.lower()
                if (query_lower not in metadata["name"].lower() and 
                    query_lower not in metadata["description"].lower()):
                    continue
            
            resource = Resource(
                uri=f"kb://{kb_dir}",
                title=metadata["name"],
                description=metadata["description"]
            )
            resources.append(resource)
        
        return resources

    def query_relevant_documents(self, query: str, resources: List[Resource] = []) -> List[Document]:
        """Query relevant documents from specified knowledge bases."""
        if not resources:
            return []
        
        all_documents = []
        for resource in resources:
            kb_id = parse_kb_uri(resource.uri)
            if kb_id:
                docs = self.vector_search_manager.search_in_kb(kb_id, query)
                all_documents.extend(docs)
        
        # Sort by similarity and return top results
        all_documents.sort(
            key=lambda x: max(chunk.similarity for chunk in x.chunks) if x.chunks else 0, 
            reverse=True
        )
        return all_documents[:self.max_results]

    def create_knowledge_base(self, name: str, description: str = "") -> str:
        """Create a new knowledge base."""
        kb_id = name.lower().replace(" ", "_").replace("-", "_")
        kb_path = os.path.join(self.appdata_path, kb_id)
        
        # Create directory structure
        os.makedirs(kb_path, exist_ok=True)
        setup_kb_directories(kb_path)
        
        # Create metadata
        metadata = {
            "id": kb_id,
            "name": name,
            "description": description,
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat(),
            "document_count": 0,
            "documents": []
        }
        
        self.metadata_manager.save_kb_metadata(kb_path, metadata)
        return kb_id

    def get_knowledge_bases(self) -> List[Dict[str, Any]]:
        """Get list of all knowledge bases with metadata."""
        kbs = []
        
        for kb_dir in os.listdir(self.appdata_path):
            kb_path = os.path.join(self.appdata_path, kb_dir)
            if not os.path.isdir(kb_path):
                continue
                
            lancedb_path = os.path.join(kb_path, "lancedb")
            if os.path.exists(lancedb_path):
                metadata = self.metadata_manager.get_kb_metadata(kb_path)
                metadata["id"] = kb_dir
                kbs.append(metadata)
        
        return kbs

    def get_documents(self, kb_id: str) -> List[Dict[str, Any]]:
        """Get list of documents in a knowledge base from metadata."""
        kb_path = os.path.join(self.appdata_path, kb_id)
        
        if not os.path.exists(kb_path):
            return []
        
        # Sync metadata with file system
        self.metadata_manager.sync_documents_metadata(kb_id)
        
        # Get updated metadata
        metadata = self.metadata_manager.get_kb_metadata(kb_path)
        return metadata.get("documents", [])

    def delete_knowledge_base(self, kb_id: str) -> bool:
        """Delete entire knowledge base including all files and data."""
        try:
            kb_path = os.path.join(self.appdata_path, kb_id)
            
            if not os.path.exists(kb_path):
                print(f"Knowledge base not found: {kb_id}")
                return False
            
            shutil.rmtree(kb_path)
            print(f"Successfully deleted knowledge base: {kb_id}")
            return True
            
        except Exception as e:
            print(f"Error deleting knowledge base {kb_id}: {e}")
            return False

    async def process_document(self, kb_id: str, filename: str) -> bool:
        """Process document: convert to markdown and index into vector database."""
        try:
            # Update status to processing
            self.metadata_manager.update_document_status(kb_id, filename, "processing")
            
            # Add small delay for UX
            await asyncio.sleep(1)
            
            await self._process_document_steps(kb_id, filename)
            
            # Update status to ready
            self.metadata_manager.update_document_status(kb_id, filename, "ready")
            print(f"Successfully processed document: {filename}")
            return True
            
        except Exception as e:
            error_message = str(e)
            self.metadata_manager.update_document_status(kb_id, filename, "error", error_message)
            print(f"Error processing document {filename}: {error_message}")
            print(f"Full error traceback for {filename}:")
            print(traceback.format_exc())
            return False

    async def _process_document_steps(self, kb_id: str, filename: str) -> None:
        """Execute the document processing steps."""
        kb_path = os.path.join(self.appdata_path, kb_id)
        documents_dir = os.path.join(kb_path, "documents")
        markdown_dir = os.path.join(kb_path, "markdown")
        lancedb_dir = os.path.join(kb_path, "lancedb")
        
        # Ensure directories exist
        os.makedirs(markdown_dir, exist_ok=True)
        os.makedirs(lancedb_dir, exist_ok=True)
        
        file_path = os.path.join(documents_dir, filename)
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Document not found: {filename}")
        
        # Convert to markdown
        print(f"Converting {filename} to markdown...")
        markdown_content = await self.document_processor.convert_to_markdown(file_path, filename)
        
        # Save markdown file
        file_base = os.path.splitext(filename)[0]
        markdown_path = os.path.join(markdown_dir, f"{file_base}.md")
        with open(markdown_path, 'w', encoding='utf-8') as f:
            f.write(markdown_content)
        
        # Create embeddings
        print(f"Initializing embeddings for {filename}...")
        embedding_model = os.getenv("EMBEDDING_MODEL", "nomic-embed-text:latest")
        embeddings = await self.document_processor.create_embeddings(embedding_model)
        
        # Chunk document
        print(f"Chunking {filename}...")
        chunks = await self.document_processor.chunk_document(
            markdown_content, filename, kb_id, embeddings
        )
        print(f"Successfully chunked {filename} into {len(chunks)} chunks")
        
        # Index into vector database
        print(f"Indexing {filename} into vector database...")
        await self.document_processor.index_to_vectorstore(chunks, lancedb_dir, embeddings)
        print(f"Successfully indexed {filename} into vector database")

    def delete_document_complete(self, kb_id: str, filename: str) -> bool:
        """Complete document deletion including files, metadata, and vectorstore."""
        try:
            kb_path = os.path.join(self.appdata_path, kb_id)
            
            # Delete physical files
            files_deleted = self._delete_document_files(kb_path, filename)
            
            # Remove from vectorstore
            vectorstore_deleted = self.document_processor.delete_from_vectorstore(kb_id, filename)
            
            # Remove from metadata (do this last)
            self.metadata_manager.remove_document_metadata(kb_id, filename)
            
            print(f"Document deletion summary for {filename}:")
            print(f"  - Files deleted: {', '.join(files_deleted) if files_deleted else 'none'}")
            print(f"  - Vectorstore deleted: {'yes' if vectorstore_deleted else 'no'}")
            print(f"  - Metadata updated: yes")
            
            return True
            
        except Exception as e:
            print(f"Error during complete document deletion: {e}")
            return False

    def _delete_document_files(self, kb_path: str, filename: str) -> List[str]:
        """Delete document and markdown files."""
        files_deleted = []
        
        # Delete document file
        doc_file = os.path.join(kb_path, "documents", filename)
        if os.path.exists(doc_file):
            os.remove(doc_file)
            files_deleted.append("document file")
        
        # Delete markdown file
        file_base = os.path.splitext(filename)[0]
        markdown_file = os.path.join(kb_path, "markdown", f"{file_base}.md")
        if os.path.exists(markdown_file):
            os.remove(markdown_file)
            files_deleted.append("markdown file")
        
        return files_deleted

    # Delegate methods to managers
    def update_document_status(self, kb_id: str, filename: str, status: str, error_message: str = ""):
        """Update document processing status."""
        return self.metadata_manager.update_document_status(kb_id, filename, status, error_message)

    def get_document_status(self, kb_id: str, filename: str) -> Optional[Dict[str, Any]]:
        """Get status of a specific document."""
        return self.metadata_manager.get_document_status(kb_id, filename) 