#!/usr/bin/env python3
"""
Test script để kiểm tra Documents API
"""

import os
import sys
import requests
import json
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

def test_documents_api():
    """Test documents API endpoints"""
    
    base_url = "http://localhost:8000"
    
    print("🧪 Testing Documents API...")
    print("=" * 50)
    
    # Test 1: List knowledge bases
    print("\n📋 Test 1: List Knowledge Bases")
    try:
        response = requests.get(f"{base_url}/api/knowledge-bases")
        if response.status_code == 200:
            kbs = response.json()
            print(f"✅ Found {len(kbs)} knowledge bases")
            
            for kb in kbs:
                print(f"   - {kb['name']} (ID: {kb['id']})")
                print(f"     Documents: {kb['document_count']}")
                
                # Test documents for this KB
                print(f"\n📄 Test 2: List Documents for KB '{kb['id']}'")
                doc_response = requests.get(f"{base_url}/api/knowledge-bases/{kb['id']}/documents")
                
                if doc_response.status_code == 200:
                    docs = doc_response.json()
                    print(f"✅ Found {len(docs)} documents")
                    
                    for doc in docs:
                        print(f"   - {doc['name']} ({doc['file_name']})")
                        print(f"     Size: {doc['file_size']} bytes")
                        print(f"     Type: {doc['file_type']}")
                        print(f"     Status: {doc['status']}")
                else:
                    print(f"❌ Failed to get documents: {doc_response.status_code}")
                    print(f"   Error: {doc_response.text}")
        else:
            print(f"❌ Failed to get knowledge bases: {response.status_code}")
            print(f"   Error: {response.text}")
            
    except requests.exceptions.ConnectionError:
        print("❌ Cannot connect to server. Make sure backend is running:")
        print("   uv run python server.py")
    except Exception as e:
        print(f"❌ Error: {e}")

def test_local_provider():
    """Test LocalKnowledgeBaseProvider directly"""
    
    print("\n🔧 Testing LocalKnowledgeBaseProvider directly...")
    print("=" * 60)
    
    try:
        from rag.local_knowledge_base import LocalKnowledgeBaseProvider
        
        # Initialize provider
        provider = LocalKnowledgeBaseProvider()
        
        # Test get knowledge bases
        kbs = provider.get_knowledge_bases()
        print(f"📋 Found {len(kbs)} knowledge bases")
        
        for kb in kbs:
            print(f"\n📚 Knowledge Base: {kb['name']}")
            print(f"   ID: {kb['id']}")
            print(f"   Document Count: {kb['document_count']}")
            
            # Test get documents
            docs = provider.get_documents(kb['id'])
            print(f"   📄 Found {len(docs)} documents:")
            
            for doc in docs:
                print(f"      - {doc['name']}")
                print(f"        File: {doc['file_name']}")
                print(f"        Size: {doc['file_size']} bytes")
                print(f"        Type: {doc['file_type']}")
                print(f"        Status: {doc['status']}")
        
        print("\n✅ LocalKnowledgeBaseProvider test completed!")
        
    except Exception as e:
        print(f"❌ LocalKnowledgeBaseProvider test failed: {e}")

def main():
    """Main test function"""
    print("🚀 Testing Documents Functionality")
    print("=" * 60)
    
    # Test provider directly first
    test_local_provider()
    
    # Test API endpoints
    test_documents_api()
    
    print("\n🎉 All tests completed!")
    print("\n💡 If API tests failed, make sure:")
    print("   1. Backend is running: uv run python server.py")
    print("   2. Frontend is running: cd web && pnpm dev")
    print("   3. Visit: http://localhost:3000/knowledge-base")

if __name__ == "__main__":
    main() 