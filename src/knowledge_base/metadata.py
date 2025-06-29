# Copyright (c) 2025 Bytedance Ltd. and/or its affiliates
# SPDX-License-Identifier: MIT

import os
import json
import hashlib
from datetime import datetime
from typing import Dict, Any, Optional, List

from .utils import count_documents, get_content_type


class MetadataManager:
    """Manages knowledge base and document metadata."""
    
    def __init__(self, appdata_path: str):
        self.appdata_path = appdata_path
    
    def get_kb_metadata(self, kb_path: str) -> Dict[str, Any]:
        """Get metadata for a knowledge base."""
        metadata_file = os.path.join(kb_path, "metadata.json")
        current_doc_count = count_documents(kb_path)
        
        if os.path.exists(metadata_file):
            try:
                with open(metadata_file, 'r', encoding='utf-8') as f:
                    metadata = json.load(f)
                    metadata["document_count"] = current_doc_count
                    metadata["updated_at"] = datetime.now().isoformat()
                    
                    if "documents" not in metadata:
                        metadata["documents"] = []
                    
                    return metadata
            except Exception:
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
    
    def save_kb_metadata(self, kb_path: str, metadata: Dict[str, Any]) -> None:
        """Save metadata to file."""
        metadata_file = os.path.join(kb_path, "metadata.json")
        metadata["updated_at"] = datetime.now().isoformat()
        
        with open(metadata_file, 'w', encoding='utf-8') as f:
            json.dump(metadata, f, indent=2, ensure_ascii=False)
    
    def add_document_metadata(self, kb_id: str, filename: str) -> None:
        """Add new document metadata."""
        kb_path = os.path.join(self.appdata_path, kb_id)
        docs_path = os.path.join(kb_path, "documents")
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
        content_type = get_content_type(file_ext)
        
        document = {
            "id": doc_id,
            "knowledge_base_id": kb_id,
            "name": os.path.splitext(filename)[0],
            "file_name": filename,
            "file_type": content_type,
            "file_size": file_size,
            "status": "pending",
            "error_message": "",
            "created_at": created_time.isoformat(),
            "updated_at": modified_time.isoformat(),
            "processing_started_at": None,
            "processing_completed_at": None
        }
        
        # Add to metadata
        metadata = self.get_kb_metadata(kb_path)
        metadata["documents"].append(document)
        metadata["document_count"] = len(metadata["documents"])
        
        self.save_kb_metadata(kb_path, metadata)
    
    def update_document_status(self, kb_id: str, filename: str, status: str, 
                             error_message: str = "") -> None:
        """Update document processing status."""
        kb_path = os.path.join(self.appdata_path, kb_id)
        metadata = self.get_kb_metadata(kb_path)
        
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
        
        self.save_kb_metadata(kb_path, metadata)
    
    def get_document_status(self, kb_id: str, filename: str) -> Optional[Dict[str, Any]]:
        """Get status of a specific document."""
        kb_path = os.path.join(self.appdata_path, kb_id)
        metadata = self.get_kb_metadata(kb_path)
        
        for doc in metadata["documents"]:
            if doc["file_name"] == filename:
                return doc
        
        return None
    
    def remove_document_metadata(self, kb_id: str, filename: str) -> None:
        """Remove document metadata when file is deleted."""
        kb_path = os.path.join(self.appdata_path, kb_id)
        metadata = self.get_kb_metadata(kb_path)
        
        metadata["documents"] = [
            doc for doc in metadata["documents"] 
            if doc["file_name"] != filename
        ]
        metadata["document_count"] = len(metadata["documents"])
        
        self.save_kb_metadata(kb_path, metadata)
    
    def sync_documents_metadata(self, kb_id: str) -> None:
        """Sync document metadata with actual files in the file system."""
        kb_path = os.path.join(self.appdata_path, kb_id)
        docs_path = os.path.join(kb_path, "documents")
        
        if not os.path.exists(docs_path):
            return
        
        metadata = self.get_kb_metadata(kb_path)
        documents_dict = {doc["file_name"]: doc for doc in metadata.get("documents", [])}
        
        # Scan actual files in documents directory
        current_files = set()
        for filename in os.listdir(docs_path):
            file_path = os.path.join(docs_path, filename)
            
            if os.path.isfile(file_path) and not filename.startswith('.'):
                current_files.add(filename)
                
                if filename in documents_dict:
                    # Update existing document
                    doc = documents_dict[filename]
                    stat = os.stat(file_path)
                    
                    if doc["file_size"] != stat.st_size:
                        doc["file_size"] = stat.st_size
                        doc["updated_at"] = datetime.fromtimestamp(stat.st_mtime).isoformat()
                else:
                    # Add new document
                    self.add_document_metadata(kb_id, filename)
        
        # Remove documents that no longer exist in file system
        metadata["documents"] = [
            doc for doc in metadata["documents"] 
            if doc["file_name"] in current_files
        ]
        metadata["document_count"] = len(metadata["documents"])
        
        self.save_kb_metadata(kb_path, metadata) 