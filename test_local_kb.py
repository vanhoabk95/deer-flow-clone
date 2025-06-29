#!/usr/bin/env python3
"""
Test script cho Local Knowledge Base Provider
"""

import os
import sys
import asyncio
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from src.knowledge_base import LocalKnowledgeBaseProvider
from rag.retriever import Resource


async def test_local_knowledge_base():
    """Test local knowledge base functionality"""
    
    print("🧪 Testing Local Knowledge Base Provider...")
    print("=" * 50)
    
    # Initialize provider
    provider = LocalKnowledgeBaseProvider()
    
    # Test 1: List resources
    print("\n📋 Test 1: List all knowledge bases")
    resources = provider.list_resources()
    print(f"Found {len(resources)} knowledge bases:")
    for resource in resources:
        print(f"  - {resource.title} ({resource.uri})")
        print(f"    Description: {resource.description}")
    
    if not resources:
        print("❌ No knowledge bases found. Creating a test knowledge base...")
        kb_id = provider.create_knowledge_base(
            "Test Knowledge Base", 
            "Automatically created for testing"
        )
        print(f"✅ Created knowledge base: {kb_id}")
        resources = provider.list_resources()
    
    # Test 2: Search with query
    print("\n🔍 Test 2: Search knowledge bases")
    search_resources = provider.list_resources("test")
    print(f"Found {len(search_resources)} knowledge bases matching 'test':")
    for resource in search_resources:
        print(f"  - {resource.title}")
    
    # Test 3: Query documents (if knowledge base exists)
    if resources:
        print("\n📄 Test 3: Query documents")
        test_resource = resources[0]
        print(f"Testing with knowledge base: {test_resource.title}")
        
        try:
            documents = provider.query_relevant_documents(
                "test query", 
                [test_resource]
            )
            print(f"Found {len(documents)} documents")
            for doc in documents:
                print(f"  - Document: {doc.title}")
                print(f"    Chunks: {len(doc.chunks)}")
                if doc.chunks:
                    print(f"    First chunk preview: {doc.chunks[0].content[:100]}...")
        except Exception as e:
            print(f"⚠️  Error querying documents: {e}")
            print("This might be normal if LanceDB is not properly set up or Ollama is not running")
    
    # Test 4: Get knowledge bases metadata
    print("\n📊 Test 4: Get knowledge bases metadata")
    kbs = provider.get_knowledge_bases()
    print(f"Found {len(kbs)} knowledge bases with metadata:")
    for kb in kbs:
        print(f"  - {kb['name']} (ID: {kb['id']})")
        print(f"    Documents: {kb['document_count']}")
        print(f"    Created: {kb['created_at']}")
    
    print("\n✅ All tests completed!")


def test_builder():
    """Test RAG builder with local provider"""
    print("\n🔧 Testing RAG Builder...")
    
    # Import builder
    from rag.builder import build_retriever
    from config.tools import SELECTED_RAG_PROVIDER
    
    print(f"Selected RAG provider: {SELECTED_RAG_PROVIDER}")
    
    retriever = build_retriever()
    if retriever:
        print(f"✅ Successfully created retriever: {type(retriever).__name__}")
        
        # Test list resources
        resources = retriever.list_resources()
        print(f"📋 Found {len(resources)} resources via builder")
    else:
        print("❌ Failed to create retriever")


def test_tool_integration():
    """Test retriever tool integration"""
    print("\n🛠️  Testing Tool Integration...")
    
    from tools.retriever import get_retriever_tool
    from rag.retriever import Resource
    
    # Create test resources
    test_resources = [
        Resource(
            uri="kb://knowledge_base_test",
            title="Test Knowledge Base",
            description="Test description"
        )
    ]
    
    # Get retriever tool
    tool = get_retriever_tool(test_resources)
    
    if tool:
        print(f"✅ Successfully created retriever tool: {tool.name}")
        print(f"📝 Tool description: {tool.description}")
        
        # Test tool invocation
        try:
            result = tool._run("test query")
            print(f"🔍 Tool result type: {type(result)}")
            if isinstance(result, list):
                print(f"📄 Found {len(result)} results")
            else:
                print(f"📄 Result: {result}")
        except Exception as e:
            print(f"⚠️  Error invoking tool: {e}")
    else:
        print("❌ Failed to create retriever tool")


async def main():
    """Main test function"""
    print("🚀 Starting Local Knowledge Base Tests")
    print("=" * 60)
    
    # Test provider directly
    await test_local_knowledge_base()
    
    # Test builder
    test_builder()
    
    # Test tool integration
    test_tool_integration()
    
    print("\n🎉 All tests completed!")
    print("\n💡 Tips:")
    print("  - Make sure Ollama is running with nomic-embed-text model")
    print("  - Check that appdata/knowledge_base_test exists")
    print("  - Verify LanceDB data is properly indexed")


if __name__ == "__main__":
    asyncio.run(main()) 