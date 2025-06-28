#!/usr/bin/env python3
"""
Simple test script để debug Local Knowledge Base
"""

import os
import sys
import asyncio
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

def test_imports():
    """Test basic imports"""
    print("🔍 Testing imports...")
    
    try:
        from rag.local_knowledge_base import LocalKnowledgeBaseProvider
        print("✅ LocalKnowledgeBaseProvider import OK")
    except Exception as e:
        print(f"❌ LocalKnowledgeBaseProvider import failed: {e}")
        return False
    
    try:
        from rag.retriever import Resource, Document, Chunk
        print("✅ Retriever classes import OK")
    except Exception as e:
        print(f"❌ Retriever classes import failed: {e}")
        return False
    
    try:
        from rag.builder import build_retriever
        print("✅ build_retriever import OK")
    except Exception as e:
        print(f"❌ build_retriever import failed: {e}")
        return False
    
    return True

def test_provider_basic():
    """Test basic provider functionality"""
    print("\n📋 Testing LocalKnowledgeBaseProvider basic functions...")
    
    try:
        from rag.local_knowledge_base import LocalKnowledgeBaseProvider
        
        # Initialize provider
        provider = LocalKnowledgeBaseProvider()
        print(f"✅ Provider initialized, appdata_path: {provider.appdata_path}")
        
        # Test list resources
        resources = provider.list_resources()
        print(f"✅ Found {len(resources)} knowledge bases")
        
        for resource in resources:
            print(f"   - {resource.title} ({resource.uri})")
        
        return True
        
    except Exception as e:
        print(f"❌ Provider test failed: {e}")
        return False

def test_builder():
    """Test RAG builder"""
    print("\n🔧 Testing RAG builder...")
    
    try:
        from rag.builder import build_retriever
        from config.tools import SELECTED_RAG_PROVIDER
        
        print(f"Selected RAG provider: {SELECTED_RAG_PROVIDER}")
        
        retriever = build_retriever()
        if retriever:
            print(f"✅ Retriever created: {type(retriever).__name__}")
            return True
        else:
            print("❌ Retriever is None")
            return False
            
    except Exception as e:
        print(f"❌ Builder test failed: {e}")
        return False

def test_resource_creation():
    """Test Resource object creation"""
    print("\n📦 Testing Resource creation...")
    
    try:
        from rag.retriever import Resource
        
        # Create Resource manually
        resource = Resource(
            uri="kb://test",
            title="Test KB",
            description="Test description"
        )
        
        print(f"✅ Resource created: {resource.title}")
        print(f"   URI: {resource.uri}")
        print(f"   Description: {resource.description}")
        
        # Test serialization
        data = resource.model_dump()
        print(f"✅ Resource serialized: {data}")
        
        # Test deserialization
        new_resource = Resource(**data)
        print(f"✅ Resource deserialized: {new_resource.title}")
        
        return True
        
    except Exception as e:
        print(f"❌ Resource creation failed: {e}")
        return False

def test_tool_creation_simple():
    """Test simple tool creation without Pydantic validation"""
    print("\n🛠️  Testing simple tool creation...")
    
    try:
        from rag.retriever import Resource
        from rag.builder import build_retriever
        
        # Create test resource
        resource = Resource(
            uri="kb://knowledge_base_test",
            title="Test KB",
            description="Test description"
        )
        
        print(f"✅ Test resource created: {resource.title}")
        
        # Get retriever
        retriever = build_retriever()
        print(f"✅ Retriever obtained: {type(retriever).__name__}")
        
        # Manual tool-like test
        if retriever and hasattr(retriever, 'query_relevant_documents'):
            print("✅ Retriever has query_relevant_documents method")
            
            # Test basic query (simplified)
            try:
                result = retriever.query_relevant_documents("test", [resource])
                print(f"✅ Query executed, found {len(result)} documents")
            except Exception as e:
                print(f"⚠️  Query failed (might be normal): {e}")
        
        return True
        
    except Exception as e:
        print(f"❌ Simple tool test failed: {e}")
        return False

def main():
    """Main test function"""
    print("🚀 Simple Local Knowledge Base Debug")
    print("=" * 50)
    
    # Test imports first
    if not test_imports():
        print("\n❌ Import tests failed, stopping")
        return
    
    # Test provider
    if not test_provider_basic():
        print("\n❌ Provider tests failed, stopping")
        return
    
    # Test builder
    if not test_builder():
        print("\n❌ Builder tests failed, stopping")
        return
    
    # Test resource creation
    if not test_resource_creation():
        print("\n❌ Resource tests failed, stopping")
        return
    
    # Test simple tool creation
    if not test_tool_creation_simple():
        print("\n❌ Tool tests failed")
        return
    
    print("\n✅ All basic tests passed!")
    print("\n💡 Now you can try the full test: uv run python test_local_kb.py")

if __name__ == "__main__":
    main() 