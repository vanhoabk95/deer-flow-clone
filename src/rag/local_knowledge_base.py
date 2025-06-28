# Copyright (c) 2025 Bytedance Ltd. and/or its affiliates
# SPDX-License-Identifier: MIT

import os
import json
import hashlib
from pathlib import Path
from typing import List, Dict, Any, Optional
from datetime import datetime

from src.rag.retriever import Chunk, Document, Resource, Retriever
from urllib.parse import urlparse


class LocalKnowledgeBaseProvider(Retriever):
    """
    LocalKnowledgeBaseProvider uses local LanceDB and file system for knowledge base management.
    """

    appdata_path: str
    max_results: int = 10

    def __init__(self):
        self.appdata_path = os.path.join(os.getcwd(), "appdata")
        if not os.path.exists(self.appdata_path):
            os.makedirs(self.appdata_path)
        self.max_results = int(os.getenv("LOCAL_KB_MAX_RESULTS", "10"))

    def list_resources(self, query: str | None = None) -> List[Resource]:
        """List all knowledge bases as resources."""
        resources = []
        
        # Scan appdata directory for knowledge bases
        for kb_dir in os.listdir(self.appdata_path):
            kb_path = os.path.join(self.appdata_path, kb_dir)
            if os.path.isdir(kb_path):
                # Check if this is a valid knowledge base (has lancedb directory)
                lancedb_path = os.path.join(kb_path, "lancedb")
                if os.path.exists(lancedb_path):
                    # Try to get metadata
                    metadata = self._get_kb_metadata(kb_path)
                    
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
        all_documents = []
        
        # If no resources specified, return empty
        if not resources:
            return []
        
        # Process each knowledge base resource
        for resource in resources:
            kb_id = self._parse_kb_uri(resource.uri)
            if kb_id:
                docs = self._search_in_kb(kb_id, query)
                all_documents.extend(docs)
        
        # Sort by similarity and return top results
        all_documents.sort(key=lambda x: max(chunk.similarity for chunk in x.chunks) if x.chunks else 0, reverse=True)
        return all_documents[:self.max_results]

    def _get_kb_metadata(self, kb_path: str) -> Dict[str, Any]:
        """Get metadata for a knowledge base."""
        metadata_file = os.path.join(kb_path, "metadata.json")
        
        # Always get current document count
        current_doc_count = self._count_documents(kb_path)
        
        if os.path.exists(metadata_file):
            try:
                with open(metadata_file, 'r', encoding='utf-8') as f:
                    metadata = json.load(f)
                    # Update document count to current value
                    metadata["document_count"] = current_doc_count
                    metadata["updated_at"] = datetime.now().isoformat()
                    
                    # Ensure documents array exists
                    if "documents" not in metadata:
                        metadata["documents"] = []
                    
                    return metadata
            except:
                pass
        
        # Default metadata if file doesn't exist
        kb_name = os.path.basename(kb_path)
        return {
            "id": kb_name,
            "name": kb_name.replace("_", " ").title(),
            "description": f"Knowledge base: {kb_name}",
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat(),
            "document_count": current_doc_count,
            "documents": []
        }

    def _save_kb_metadata(self, kb_path: str, metadata: Dict[str, Any]):
        """Save metadata to file."""
        metadata_file = os.path.join(kb_path, "metadata.json")
        metadata["updated_at"] = datetime.now().isoformat()
        
        with open(metadata_file, 'w', encoding='utf-8') as f:
            json.dump(metadata, f, indent=2, ensure_ascii=False)

    def _count_documents(self, kb_path: str) -> int:
        """Count documents in knowledge base."""
        docs_path = os.path.join(kb_path, "documents")
        if os.path.exists(docs_path):
            return len([f for f in os.listdir(docs_path) 
                       if os.path.isfile(os.path.join(docs_path, f)) and not f.startswith('.')])
        return 0

    def _parse_kb_uri(self, uri: str) -> str | None:
        """Parse knowledge base URI to extract KB ID."""
        try:
            parsed = urlparse(uri)
            if parsed.scheme == "kb":
                return parsed.netloc or parsed.path.strip("/")
        except:
            pass
        return None

    def _search_in_kb(self, kb_id: str, query: str) -> List[Document]:
        """Search documents in a specific knowledge base using LanceDB."""
        kb_path = os.path.join(self.appdata_path, kb_id)
        lancedb_path = os.path.join(kb_path, "lancedb")
        
        if not os.path.exists(lancedb_path):
            return []
        
        try:
            # Import LanceDB dependencies
            import lancedb
            from langchain_community.vectorstores import LanceDB
            from langchain_ollama import OllamaEmbeddings
            
            # Initialize embeddings - using Ollama as default
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
            documents = []
            doc_groups = {}  # Group chunks by document
            
            for lc_doc in langchain_docs:
                # Extract document info from metadata
                metadata = lc_doc.metadata
                doc_id = metadata.get("source", f"doc_{hashlib.md5(lc_doc.page_content.encode()).hexdigest()[:8]}")
                doc_title = metadata.get("title", doc_id)
                
                # Calculate similarity (placeholder - LanceDB doesn't directly provide this)
                similarity = metadata.get("similarity", 0.8)
                
                if doc_id not in doc_groups:
                    doc_groups[doc_id] = Document(
                        id=doc_id,
                        title=doc_title,
                        chunks=[]
                    )
                
                chunk = Chunk(
                    content=lc_doc.page_content,
                    similarity=similarity
                )
                doc_groups[doc_id].chunks.append(chunk)
            
            documents = list(doc_groups.values())
            return documents
            
        except Exception as e:
            print(f"Error searching in knowledge base {kb_id}: {e}")
            return []

    def create_knowledge_base(self, name: str, description: str = "") -> str:
        """Create a new knowledge base."""
        # Generate KB ID from name
        kb_id = name.lower().replace(" ", "_").replace("-", "_")
        kb_path = os.path.join(self.appdata_path, kb_id)
        
        # Create directory structure
        os.makedirs(kb_path, exist_ok=True)
        os.makedirs(os.path.join(kb_path, "documents"), exist_ok=True)
        os.makedirs(os.path.join(kb_path, "markdown"), exist_ok=True)
        os.makedirs(os.path.join(kb_path, "lancedb"), exist_ok=True)
        
        # Create metadata with documents array
        metadata = {
            "id": kb_id,
            "name": name,
            "description": description,
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat(),
            "document_count": 0,
            "documents": []
        }
        
        self._save_kb_metadata(kb_path, metadata)
        return kb_id

    def get_knowledge_bases(self) -> List[Dict[str, Any]]:
        """Get list of all knowledge bases with metadata."""
        kbs = []
        
        for kb_dir in os.listdir(self.appdata_path):
            kb_path = os.path.join(self.appdata_path, kb_dir)
            if os.path.isdir(kb_path):
                lancedb_path = os.path.join(kb_path, "lancedb")
                if os.path.exists(lancedb_path):
                    metadata = self._get_kb_metadata(kb_path)
                    metadata["id"] = kb_dir
                    kbs.append(metadata)
        
        return kbs

    def get_documents(self, kb_id: str) -> List[Dict[str, Any]]:
        """Get list of documents in a knowledge base from metadata."""
        kb_path = os.path.join(self.appdata_path, kb_id)
        
        if not os.path.exists(kb_path):
            return []
        
        metadata = self._get_kb_metadata(kb_path)
        
        # Sync file system with metadata
        self._sync_documents_metadata(kb_id)
        
        # Reload metadata after sync
        metadata = self._get_kb_metadata(kb_path)
        
        return metadata.get("documents", [])

    def _sync_documents_metadata(self, kb_id: str):
        """Sync document metadata with actual files in the file system."""
        kb_path = os.path.join(self.appdata_path, kb_id)
        docs_path = os.path.join(kb_path, "documents")
        markdown_path = os.path.join(kb_path, "markdown")
        
        if not os.path.exists(docs_path):
            return
        
        metadata = self._get_kb_metadata(kb_path)
        documents_dict = {doc["file_name"]: doc for doc in metadata.get("documents", [])}
        
        # Scan actual files in documents directory
        current_files = set()
        for filename in os.listdir(docs_path):
            file_path = os.path.join(docs_path, filename)
            
            if os.path.isfile(file_path) and not filename.startswith('.'):
                current_files.add(filename)
                
                # Update or create document metadata
                if filename in documents_dict:
                    # Update existing document
                    doc = documents_dict[filename]
                    stat = os.stat(file_path)
                    
                    # Update file size and modified time if changed
                    if doc["file_size"] != stat.st_size:
                        doc["file_size"] = stat.st_size
                        doc["updated_at"] = datetime.fromtimestamp(stat.st_mtime).isoformat()
                    
                    # Check markdown status
                    markdown_file = os.path.join(markdown_path, f"{os.path.splitext(filename)[0]}.md")
                    if os.path.exists(markdown_file) and doc["status"] != "ready":
                        doc["status"] = "ready"
                        doc["error_message"] = ""
                        doc["updated_at"] = datetime.now().isoformat()
                else:
                    # Add new document
                    self._add_document_metadata(kb_id, filename)
        
        # Remove documents that no longer exist in file system
        metadata["documents"] = [doc for doc in metadata["documents"] 
                               if doc["file_name"] in current_files]
        
        # Update document count
        metadata["document_count"] = len(metadata["documents"])
        
        # Save updated metadata
        self._save_kb_metadata(kb_path, metadata)

    def _add_document_metadata(self, kb_id: str, filename: str):
        """Add new document metadata."""
        kb_path = os.path.join(self.appdata_path, kb_id)
        docs_path = os.path.join(kb_path, "documents")
        markdown_path = os.path.join(kb_path, "markdown")
        file_path = os.path.join(docs_path, filename)
        
        if not os.path.exists(file_path):
            return
        
        # Get file stats
        stat = os.stat(file_path)
        file_size = stat.st_size
        created_time = datetime.fromtimestamp(stat.st_ctime)
        modified_time = datetime.fromtimestamp(stat.st_mtime)
        
        # Generate document ID from filename
        doc_id = f"doc_{hashlib.md5(filename.encode()).hexdigest()[:8]}"
        
        # Determine file type
        file_ext = os.path.splitext(filename)[1].lower()
        content_type = self._get_content_type(file_ext)
        
        # Check if markdown version exists
        markdown_file = os.path.join(markdown_path, f"{os.path.splitext(filename)[0]}.md")
        status = "ready" if os.path.exists(markdown_file) else "pending"
        
        document = {
            "id": doc_id,
            "knowledge_base_id": kb_id,
            "name": os.path.splitext(filename)[0],
            "file_name": filename,
            "file_type": content_type,
            "file_size": file_size,
            "status": status,
            "error_message": "",
            "created_at": created_time.isoformat(),
            "updated_at": modified_time.isoformat(),
            "processing_started_at": None,
            "processing_completed_at": None
        }
        
        # Add to metadata
        metadata = self._get_kb_metadata(kb_path)
        metadata["documents"].append(document)
        metadata["document_count"] = len(metadata["documents"])
        
        self._save_kb_metadata(kb_path, metadata)

    def update_document_status(self, kb_id: str, filename: str, status: str, error_message: str = ""):
        """Update document processing status."""
        kb_path = os.path.join(self.appdata_path, kb_id)
        metadata = self._get_kb_metadata(kb_path)
        
        # Find and update document
        for doc in metadata["documents"]:
            if doc["file_name"] == filename:
                old_status = doc["status"]
                doc["status"] = status
                doc["error_message"] = error_message
                doc["updated_at"] = datetime.now().isoformat()
                
                # Update processing timestamps
                if status == "processing" and old_status != "processing":
                    doc["processing_started_at"] = datetime.now().isoformat()
                elif status in ["ready", "error"] and old_status == "processing":
                    doc["processing_completed_at"] = datetime.now().isoformat()
                
                break
        
        self._save_kb_metadata(kb_path, metadata)

    def get_document_status(self, kb_id: str, filename: str) -> Optional[Dict[str, Any]]:
        """Get status of a specific document."""
        kb_path = os.path.join(self.appdata_path, kb_id)
        metadata = self._get_kb_metadata(kb_path)
        
        for doc in metadata["documents"]:
            if doc["file_name"] == filename:
                return doc
        
        return None

    def remove_document_metadata(self, kb_id: str, filename: str):
        """Remove document metadata when file is deleted."""
        kb_path = os.path.join(self.appdata_path, kb_id)
        metadata = self._get_kb_metadata(kb_path)
        
        # Remove document from metadata
        metadata["documents"] = [doc for doc in metadata["documents"] 
                               if doc["file_name"] != filename]
        metadata["document_count"] = len(metadata["documents"])
        
        self._save_kb_metadata(kb_path, metadata)

    def delete_document_from_vectorstore(self, kb_id: str, filename: str) -> bool:
        """Delete document vectors from LanceDB vectorstore."""
        kb_path = os.path.join(self.appdata_path, kb_id)
        lancedb_path = os.path.join(kb_path, "lancedb")
        
        if not os.path.exists(lancedb_path):
            print(f"LanceDB path not found: {lancedb_path}")
            return False
        
        try:
            # Import LanceDB dependencies
            import lancedb
            
            # Connect to LanceDB
            db = lancedb.connect(lancedb_path)
            
            # Check if documents table exists
            if "documents" not in db.table_names():
                print("Documents table not found in LanceDB")
                return False
            
            table = db.open_table("documents")
            
            # Generate document source identifier (same as used when indexing)
            # This should match the metadata.source field used when adding documents
            doc_source = filename  # or could be full path depending on implementation
            
            # Delete all records with matching source
            # LanceDB uses SQL-like syntax for deletion
            deleted_count = table.delete(f"source = '{doc_source}'")
            
            print(f"Deleted {deleted_count} vector records for document: {filename}")
            return True
            
        except Exception as e:
            print(f"Error deleting document from vectorstore {kb_id}: {e}")
            return False

    def delete_document_complete(self, kb_id: str, filename: str) -> bool:
        """Complete document deletion including files, metadata, and vectorstore."""
        try:
            kb_path = os.path.join(self.appdata_path, kb_id)
            
            # Delete physical files
            doc_file = os.path.join(kb_path, "documents", filename)
            markdown_file = os.path.join(kb_path, "markdown", f"{os.path.splitext(filename)[0]}.md")
            
            files_deleted = []
            
            # Remove document file
            if os.path.exists(doc_file):
                os.remove(doc_file)
                files_deleted.append("document file")
            
            # Remove markdown file if exists
            if os.path.exists(markdown_file):
                os.remove(markdown_file)
                files_deleted.append("markdown file")
            
            # Remove from vectorstore
            vectorstore_deleted = self.delete_document_from_vectorstore(kb_id, filename)
            
            # Remove from metadata (do this last to ensure other operations complete)
            self.remove_document_metadata(kb_id, filename)
            
            print(f"Document deletion summary for {filename}:")
            print(f"  - Files deleted: {', '.join(files_deleted) if files_deleted else 'none'}")
            print(f"  - Vectorstore deleted: {'yes' if vectorstore_deleted else 'no'}")
            print(f"  - Metadata updated: yes")
            
            return True
            
        except Exception as e:
            print(f"Error during complete document deletion: {e}")
            return False

    def get_vectorstore_info(self, kb_id: str) -> Dict[str, Any]:
        """Get information about vectorstore contents for debugging."""
        kb_path = os.path.join(self.appdata_path, kb_id)
        lancedb_path = os.path.join(kb_path, "lancedb")
        
        info = {
            "kb_id": kb_id,
            "lancedb_path": lancedb_path,
            "exists": False,
            "tables": [],
            "documents_table_info": None,
            "error": None
        }
        
        if not os.path.exists(lancedb_path):
            info["error"] = "LanceDB path not found"
            return info
        
        try:
            # Import LanceDB dependencies
            import lancedb
            
            # Connect to LanceDB
            db = lancedb.connect(lancedb_path)
            info["exists"] = True
            info["tables"] = db.table_names()
            
            # Get documents table info if exists
            if "documents" in db.table_names():
                table = db.open_table("documents")
                
                # Count total records
                total_count = table.count_rows()
                
                # Get unique sources
                try:
                    # Get sample of sources to see what's in there
                    if total_count > 0:
                        sample_data = table.head(min(100, total_count)).to_pandas()
                        unique_sources = sample_data['source'].unique().tolist() if 'source' in sample_data.columns else []
                        source_counts = sample_data['source'].value_counts().to_dict() if 'source' in sample_data.columns else {}
                    else:
                        unique_sources = []
                        source_counts = {}
                    
                    info["documents_table_info"] = {
                        "total_records": total_count,
                        "unique_sources": unique_sources,
                        "source_counts": source_counts,
                        "schema": table.schema
                    }
                except Exception as e:
                    info["documents_table_info"] = {
                        "total_records": total_count,
                        "error": f"Error getting detailed info: {e}"
                    }
            
        except Exception as e:
            info["error"] = f"Error accessing LanceDB: {e}"
        
        return info

    def count_document_records(self, kb_id: str, filename: str) -> int:
        """Count how many vector records exist for a specific document."""
        kb_path = os.path.join(self.appdata_path, kb_id)
        lancedb_path = os.path.join(kb_path, "lancedb")
        
        if not os.path.exists(lancedb_path):
            return 0
        
        try:
            # Import LanceDB dependencies
            import lancedb
            
            # Connect to LanceDB
            db = lancedb.connect(lancedb_path)
            
            # Check if documents table exists
            if "documents" not in db.table_names():
                return 0
            
            table = db.open_table("documents")
            
            # Count records with matching source
            result = table.search().where(f"source = '{filename}'").limit(1000).to_pandas()
            return len(result)
            
        except Exception as e:
            print(f"Error counting document records: {e}")
            return -1

    def _get_content_type(self, file_ext: str) -> str:
        """Get MIME type from file extension."""
        content_types = {
            '.pdf': 'application/pdf',
            '.doc': 'application/msword',
            '.docx': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
            '.txt': 'text/plain',
            '.md': 'text/markdown',
            '.html': 'text/html',
            '.htm': 'text/html',
            '.csv': 'text/csv',
            '.json': 'application/json',
            '.xml': 'application/xml'
        }
        return content_types.get(file_ext, 'application/octet-stream') 