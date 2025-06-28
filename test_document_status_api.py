#!/usr/bin/env python3
"""
Test script for Document Status API endpoints
Tests the new document status management functionality
"""

import requests
import json
import os
import time
from pathlib import Path

BASE_URL = "http://localhost:8000"

def test_knowledge_base_endpoints():
    """Test knowledge base management endpoints."""
    print("=== Testing Knowledge Base Endpoints ===")
    
    # 1. List knowledge bases
    print("\n1. List knowledge bases:")
    response = requests.get(f"{BASE_URL}/api/knowledge-bases")
    print(f"Status: {response.status_code}")
    if response.status_code == 200:
        kbs = response.json()
        print(f"Found {len(kbs)} knowledge bases:")
        for kb in kbs:
            print(f"  - {kb['name']} (id: {kb['id']}, docs: {kb['document_count']})")
    else:
        print(f"Error: {response.text}")
    
    return kbs[0]["id"] if kbs else None

def test_document_endpoints(kb_id):
    """Test document management endpoints."""
    print(f"\n=== Testing Document Endpoints for KB: {kb_id} ===")
    
    # 1. List documents
    print("\n1. List documents:")
    response = requests.get(f"{BASE_URL}/api/knowledge-bases/{kb_id}/documents")
    print(f"Status: {response.status_code}")
    if response.status_code == 200:
        docs = response.json()
        print(f"Found {len(docs)} documents:")
        for doc in docs:
            print(f"  - {doc['name']}")
            print(f"    ID: {doc['id']}")
            print(f"    File: {doc['file_name']}")
            print(f"    Status: {doc['status']}")
            print(f"    Size: {doc['file_size']} bytes")
            print(f"    Created: {doc['created_at']}")
            if doc.get('processing_started_at'):
                print(f"    Processing started: {doc['processing_started_at']}")
            if doc.get('processing_completed_at'):
                print(f"    Processing completed: {doc['processing_completed_at']}")
            if doc.get('error_message'):
                print(f"    Error: {doc['error_message']}")
            print()
        return docs[0] if docs else None
    else:
        print(f"Error: {response.text}")
        return None

def test_document_status_endpoints(kb_id, doc):
    """Test document status management endpoints."""
    if not doc:
        print("No document available for status testing")
        return
    
    print(f"\n=== Testing Document Status Endpoints ===")
    doc_id = doc["id"]
    filename = doc["file_name"]
    
    # 1. Get document by ID
    print(f"\n1. Get document by ID ({doc_id}):")
    response = requests.get(f"{BASE_URL}/api/knowledge-bases/{kb_id}/documents/{doc_id}")
    print(f"Status: {response.status_code}")
    if response.status_code == 200:
        doc_data = response.json()
        print(f"Document found: {doc_data['name']} - Status: {doc_data['status']}")
    else:
        print(f"Error: {response.text}")
    
    # 2. Get document by filename
    print(f"\n2. Get document by filename ({filename}):")
    response = requests.get(f"{BASE_URL}/api/knowledge-bases/{kb_id}/documents/by-filename/{filename}")
    print(f"Status: {response.status_code}")
    if response.status_code == 200:
        doc_data = response.json()
        print(f"Document found: {doc_data['name']} - Status: {doc_data['status']}")
    else:
        print(f"Error: {response.text}")
    
    # 3. Update document status to processing
    print(f"\n3. Update document status to 'processing':")
    update_data = {
        "status": "processing",
        "error_message": ""
    }
    response = requests.put(
        f"{BASE_URL}/api/knowledge-bases/{kb_id}/documents/{doc_id}/status",
        json=update_data
    )
    print(f"Status: {response.status_code}")
    if response.status_code == 200:
        doc_data = response.json()
        print(f"Updated status: {doc_data['status']}")
        if doc_data.get('processing_started_at'):
            print(f"Processing started at: {doc_data['processing_started_at']}")
    else:
        print(f"Error: {response.text}")
    
    # Wait a moment
    time.sleep(2)
    
    # 4. Update document status to ready
    print(f"\n4. Update document status to 'ready':")
    update_data = {
        "status": "ready",
        "error_message": ""
    }
    response = requests.put(
        f"{BASE_URL}/api/knowledge-bases/{kb_id}/documents/{doc_id}/status",
        json=update_data
    )
    print(f"Status: {response.status_code}")
    if response.status_code == 200:
        doc_data = response.json()
        print(f"Updated status: {doc_data['status']}")
        if doc_data.get('processing_completed_at'):
            print(f"Processing completed at: {doc_data['processing_completed_at']}")
    else:
        print(f"Error: {response.text}")
    
    # 5. Test error status
    print(f"\n5. Update document status to 'error':")
    update_data = {
        "status": "error",
        "error_message": "Test error message for demonstration"
    }
    response = requests.put(
        f"{BASE_URL}/api/knowledge-bases/{kb_id}/documents/{doc_id}/status",
        json=update_data
    )
    print(f"Status: {response.status_code}")
    if response.status_code == 200:
        doc_data = response.json()
        print(f"Updated status: {doc_data['status']}")
        print(f"Error message: {doc_data['error_message']}")
    else:
        print(f"Error: {response.text}")
    
    # 6. Reset to ready
    print(f"\n6. Reset document status back to 'ready':")
    update_data = {
        "status": "ready",
        "error_message": ""
    }
    response = requests.put(
        f"{BASE_URL}/api/knowledge-bases/{kb_id}/documents/{doc_id}/status",
        json=update_data
    )
    print(f"Status: {response.status_code}")
    if response.status_code == 200:
        doc_data = response.json()
        print(f"Final status: {doc_data['status']}")
    else:
        print(f"Error: {response.text}")

def test_vectorstore_debug_endpoints(kb_id):
    """Test vectorstore debugging endpoints."""
    print(f"\n=== Testing Vectorstore Debug Endpoints ===")
    
    # 1. Get vectorstore info
    print("\n1. Get vectorstore info:")
    response = requests.get(f"{BASE_URL}/api/knowledge-bases/{kb_id}/vectorstore/info")
    print(f"Status: {response.status_code}")
    if response.status_code == 200:
        info = response.json()
        print(f"  LanceDB exists: {info.get('exists')}")
        print(f"  Tables: {info.get('tables', [])}")
        if info.get('documents_table_info'):
            doc_info = info['documents_table_info']
            print(f"  Total records: {doc_info.get('total_records', 0)}")
            print(f"  Unique sources: {len(doc_info.get('unique_sources', []))}")
            if doc_info.get('source_counts'):
                print("  Source counts:")
                for source, count in doc_info['source_counts'].items():
                    print(f"    - {source}: {count} records")
        if info.get('error'):
            print(f"  Error: {info['error']}")
    else:
        print(f"Error: {response.text}")
    
    return info if response.status_code == 200 else None

def test_document_vector_counts(kb_id):
    """Test counting vector records for documents."""
    print(f"\n=== Testing Document Vector Counts ===")
    
    # Get list of documents first
    response = requests.get(f"{BASE_URL}/api/knowledge-bases/{kb_id}/documents")
    if response.status_code != 200:
        print("Could not get documents list")
        return
    
    docs = response.json()
    
    for doc in docs:
        filename = doc['file_name']
        print(f"\n1. Count vectors for: {filename}")
        
        response = requests.get(f"{BASE_URL}/api/knowledge-bases/{kb_id}/documents/by-filename/{filename}/vector-count")
        print(f"Status: {response.status_code}")
        if response.status_code == 200:
            result = response.json()
            print(f"  Vector count: {result.get('vector_count', 'unknown')}")
            if result.get('message'):
                print(f"  Message: {result['message']}")
        else:
            print(f"Error: {response.text}")

def test_document_deletion_with_vectorstore(kb_id):
    """Test complete document deletion including vectorstore."""
    print(f"\n=== Testing Document Deletion with Vectorstore ===")
    
    # Get list of documents
    response = requests.get(f"{BASE_URL}/api/knowledge-bases/{kb_id}/documents")
    if response.status_code != 200:
        print("Could not get documents list")
        return
    
    docs = response.json()
    if not docs:
        print("No documents available for deletion test")
        return
    
    # Use the last document for deletion test
    test_doc = docs[-1]
    doc_id = test_doc["id"]
    filename = test_doc["file_name"]
    
    print(f"\nTesting deletion of: {filename} (ID: {doc_id})")
    
    # 1. Check vector count before deletion
    print(f"\n1. Vector count before deletion:")
    response = requests.get(f"{BASE_URL}/api/knowledge-bases/{kb_id}/documents/by-filename/{filename}/vector-count")
    if response.status_code == 200:
        before_count = response.json().get('vector_count', 0)
        print(f"  Before: {before_count} vectors")
    else:
        before_count = "unknown"
        print(f"  Could not get before count: {response.text}")
    
    # 2. Delete the document
    print(f"\n2. Deleting document:")
    response = requests.delete(f"{BASE_URL}/api/knowledge-bases/{kb_id}/documents/{doc_id}")
    print(f"Status: {response.status_code}")
    if response.status_code == 200:
        result = response.json()
        print(f"Message: {result.get('message', 'Document deleted')}")
    else:
        print(f"Error: {response.text}")
        return
    
    # 3. Check vector count after deletion
    print(f"\n3. Vector count after deletion:")
    response = requests.get(f"{BASE_URL}/api/knowledge-bases/{kb_id}/documents/by-filename/{filename}/vector-count")
    if response.status_code == 200:
        after_count = response.json().get('vector_count', 0)
        print(f"  After: {after_count} vectors")
        if isinstance(before_count, int) and isinstance(after_count, int):
            print(f"  Reduction: {before_count - after_count} vectors removed")
    else:
        after_count = "unknown"
        print(f"  Could not get after count: {response.text}")
    
    # 4. Verify document no longer in metadata
    print(f"\n4. Verify document removed from list:")
    response = requests.get(f"{BASE_URL}/api/knowledge-bases/{kb_id}/documents")
    if response.status_code == 200:
        remaining_docs = response.json()
        remaining_filenames = [d['file_name'] for d in remaining_docs]
        if filename in remaining_filenames:
            print(f"  ❌ Document still in list!")
        else:
            print(f"  ✅ Document successfully removed from list")
        print(f"  Remaining documents: {len(remaining_docs)}")
    else:
        print(f"  Error checking remaining documents: {response.text}")

def test_metadata_file(kb_id):
    """Test metadata.json file structure."""
    print(f"\n=== Testing Metadata File Structure ===")
    
    metadata_file = f"appdata/{kb_id}/metadata.json"
    if os.path.exists(metadata_file):
        print(f"\n1. Reading metadata file: {metadata_file}")
        with open(metadata_file, 'r', encoding='utf-8') as f:
            metadata = json.load(f)
        
        print("Metadata structure:")
        print(f"  ID: {metadata.get('id')}")
        print(f"  Name: {metadata.get('name')}")
        print(f"  Description: {metadata.get('description')}")
        print(f"  Document count: {metadata.get('document_count')}")
        print(f"  Created: {metadata.get('created_at')}")
        print(f"  Updated: {metadata.get('updated_at')}")
        
        documents = metadata.get('documents', [])
        print(f"\nDocuments in metadata ({len(documents)}):")
        for doc in documents:
            print(f"  - {doc.get('name')} ({doc.get('file_name')})")
            print(f"    Status: {doc.get('status')}")
            print(f"    Size: {doc.get('file_size')} bytes")
            if doc.get('error_message'):
                print(f"    Error: {doc.get('error_message')}")
            print()
    else:
        print(f"Metadata file not found: {metadata_file}")

def main():
    """Main test function."""
    print("Document Status API Test")
    print("=" * 50)
    
    try:
        # Test knowledge base endpoints
        kb_id = test_knowledge_base_endpoints()
        
        if not kb_id:
            print("No knowledge bases found. Cannot continue with document tests.")
            return
        
        # Test document endpoints
        doc = test_document_endpoints(kb_id)
        
        # Test document status endpoints
        test_document_status_endpoints(kb_id, doc)
        
        # Test vectorstore debug endpoints
        test_vectorstore_debug_endpoints(kb_id)
        
        # Test document vector counts
        test_document_vector_counts(kb_id)
        
        # Test metadata file
        test_metadata_file(kb_id)
        
        # Test complete document deletion (including vectorstore)
        test_document_deletion_with_vectorstore(kb_id)
        
        print("\n" + "=" * 50)
        print("Test completed successfully!")
        
    except requests.exceptions.ConnectionError:
        print("Error: Cannot connect to server. Make sure the server is running on http://localhost:8000")
    except Exception as e:
        print(f"Error during testing: {e}")

if __name__ == "__main__":
    main() 