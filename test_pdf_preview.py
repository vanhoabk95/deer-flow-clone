#!/usr/bin/env python3
"""
Test script for PDF preview functionality in local search
"""

import asyncio
import json
import os
import sys
sys.path.append('src')

from src.knowledge_base import LocalKnowledgeBaseProvider


async def test_pdf_preview():
    """Test PDF preview functionality"""
    print("=== Testing PDF Preview Functionality ===\n")
    
    # Initialize provider
    provider = LocalKnowledgeBaseProvider()
    
    # List available knowledge bases
    print("1. Available Knowledge Bases:")
    kbs = provider.get_knowledge_bases()
    for kb in kbs:
        print(f"   - {kb['id']}: {kb['name']}")
        
        # List documents in this KB
        docs = provider.get_documents(kb['id'])
        print(f"     Documents ({len(docs)}):")
        for doc in docs:
            print(f"       * {doc['file_name']} ({doc['file_type']})")
    
    if not kbs:
        print("   No knowledge bases found!")
        return
    
    # Test search functionality
    print(f"\n2. Testing search in knowledge base: {kbs[0]['id']}")
    
    # Create resources for search
    from src.rag.retriever import Resource
    resources = [
        Resource(
            uri=f"kb://{kbs[0]['id']}",
            title=kbs[0]['name'],
            description=kbs[0]['description']
        )
    ]
    
    # Search for documents
    search_query = "test phân phối chuẩn"
    print(f"   Searching for: '{search_query}'")
    
    documents = provider.query_relevant_documents(search_query, resources)
    
    if not documents:
        print("   No documents found!")
        return
    
    print(f"   Found {len(documents)} documents:")
    
    for i, doc in enumerate(documents):
        print(f"\n   Document {i+1}:")
        print(f"     ID: {doc.id}")
        print(f"     Title: {doc.title}")
        print(f"     Metadata: {doc.metadata}")
        print(f"     Chunks: {len(doc.chunks)}")
        
        # Check if it's PDF and has page info
        if doc.metadata.get('file_type', '').lower() == '.pdf':
            print(f"     📄 PDF Document detected!")
            
            # Collect page numbers from chunks
            pages = set()
            for chunk in doc.chunks:
                page_num = chunk.metadata.get('page_number')
                if page_num is not None:
                    pages.add(page_num)
            
            if pages:
                sorted_pages = sorted(list(pages))
                print(f"     📄 Pages with relevant content: {sorted_pages}")
                print(f"     📄 PDF Preview URL would be: /api/knowledge-bases/{doc.metadata.get('knowledge_base')}/documents/{doc.metadata.get('file_name')}/pdf")
            else:
                print(f"     ⚠️  No page numbers found in chunks")
        
        # Show first chunk content (preview)
        if doc.chunks:
            content_preview = doc.chunks[0].content[:100] + "..." if len(doc.chunks[0].content) > 100 else doc.chunks[0].content
            print(f"     Preview: {content_preview}")
    
    # Test retriever tool format
    print(f"\n3. Testing RetrieverTool JSON format:")
    
    from src.tools.retriever import get_retriever_tool
    tool = get_retriever_tool(resources)
    
    if tool:
        result = tool._run(search_query)
        print("   Raw tool result:")
        print(f"   {result[:200]}...")
        
        # Parse result
        try:
            parsed_result = json.loads(result)
            print(f"\n   Parsed result ({len(parsed_result)} documents):")
            
            for doc_data in parsed_result:
                print(f"     - {doc_data['title']}")
                if doc_data.get('metadata', {}).get('is_pdf'):
                    pages = doc_data['metadata'].get('pdf_pages', [])
                    print(f"       📄 PDF with pages: {pages}")
                    print(f"       📄 File: {doc_data['metadata'].get('file_name')}")
                    print(f"       📄 KB: {doc_data['metadata'].get('knowledge_base')}")
        except json.JSONDecodeError as e:
            print(f"   Error parsing JSON: {e}")


if __name__ == "__main__":
    asyncio.run(test_pdf_preview()) 