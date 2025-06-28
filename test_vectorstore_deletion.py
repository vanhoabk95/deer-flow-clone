#!/usr/bin/env python3
"""
Quick test script to verify vectorstore deletion functionality
"""

import requests
import json

BASE_URL = "http://localhost:8000"

def quick_test():
    print("🔍 Quick Vectorstore Deletion Test")
    print("=" * 50)
    
    # 1. List knowledge bases
    print("\n1. Listing knowledge bases...")
    response = requests.get(f"{BASE_URL}/api/knowledge-bases")
    if response.status_code != 200:
        print(f"❌ Cannot get knowledge bases: {response.text}")
        return
    
    kbs = response.json()
    if not kbs:
        print("❌ No knowledge bases found")
        return
    
    kb_id = kbs[0]["id"]
    print(f"✅ Using knowledge base: {kb_id}")
    
    # 2. Get vectorstore info
    print(f"\n2. Getting vectorstore info for {kb_id}...")
    response = requests.get(f"{BASE_URL}/api/knowledge-bases/{kb_id}/vectorstore/info")
    if response.status_code == 200:
        info = response.json()
        print(f"✅ LanceDB exists: {info.get('exists')}")
        print(f"✅ Tables: {info.get('tables', [])}")
        
        if info.get('documents_table_info'):
            doc_info = info['documents_table_info']
            total_records = doc_info.get('total_records', 0)
            print(f"✅ Total vector records: {total_records}")
            
            if doc_info.get('source_counts'):
                print("📋 Documents in vectorstore:")
                for source, count in doc_info['source_counts'].items():
                    print(f"   - {source}: {count} vectors")
        
        if info.get('error'):
            print(f"⚠️  Warning: {info['error']}")
    else:
        print(f"❌ Cannot get vectorstore info: {response.text}")
    
    # 3. List documents
    print(f"\n3. Listing documents in {kb_id}...")
    response = requests.get(f"{BASE_URL}/api/knowledge-bases/{kb_id}/documents")
    if response.status_code == 200:
        docs = response.json()
        print(f"✅ Found {len(docs)} documents in metadata:")
        for doc in docs:
            print(f"   - {doc['file_name']} (status: {doc['status']})")
    else:
        print(f"❌ Cannot get documents: {response.text}")
        return
    
    # 4. Count vectors for each document  
    print(f"\n4. Counting vectors for each document...")
    for doc in docs:
        filename = doc['file_name']
        response = requests.get(f"{BASE_URL}/api/knowledge-bases/{kb_id}/documents/by-filename/{filename}/vector-count")
        if response.status_code == 200:
            result = response.json()
            count = result.get('vector_count', 'unknown')
            print(f"   - {filename}: {count} vectors")
        else:
            print(f"   - {filename}: error getting count")
    
    print("\n" + "=" * 50)
    print("✅ Test completed! Check the results above.")
    print("💡 To test deletion, run the full test script: python test_document_status_api.py")

if __name__ == "__main__":
    try:
        quick_test()
    except requests.exceptions.ConnectionError:
        print("❌ Error: Cannot connect to server.")
        print("💡 Make sure the server is running: python server.py")
    except Exception as e:
        print(f"❌ Error: {e}") 