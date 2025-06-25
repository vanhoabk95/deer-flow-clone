#!/usr/bin/env python3
"""
Script đơn giản để xem dữ liệu trong knowledge base test.
Hiển thị thông tin về documents đã được index trong LanceDB.
"""

import os
import sys
from pathlib import Path

import lancedb
import pandas as pd
from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import LanceDB


def main():
    """Xem dữ liệu trong knowledge base test."""
    
    # Đường dẫn đến knowledge base
    knowledge_base_path = Path("appdata/knowledge_base_test")
    lancedb_path = knowledge_base_path / "lancedb"
    table_name = "documents"
    
    print("🔍 Knowledge Base Viewer")
    print("=" * 50)
    print(f"📂 Knowledge Base: {knowledge_base_path}")
    print(f"🗄️ LanceDB Path: {lancedb_path}")
    print(f"📊 Table Name: {table_name}")
    print()
    
    # Kiểm tra xem knowledge base có tồn tại không
    if not knowledge_base_path.exists():
        print(f"❌ Knowledge base không tồn tại: {knowledge_base_path}")
        return
    
    if not lancedb_path.exists():
        print(f"❌ LanceDB không tồn tại: {lancedb_path}")
        return
    
    try:
        # Kết nối đến LanceDB
        print("🔌 Đang kết nối đến LanceDB...")
        db = lancedb.connect(str(lancedb_path))
        
        # Liệt kê các table có sẵn
        tables = db.table_names()
        print(f"📋 Tables có sẵn: {tables}")
        
        if table_name not in tables:
            print(f"❌ Table '{table_name}' không tồn tại!")
            return
        
        # Mở table
        table = db.open_table(table_name)
        
        # Thống kê cơ bản
        total_rows = table.count_rows()
        print(f"📊 Tổng số documents: {total_rows}")
        
        if total_rows == 0:
            print("📭 Không có document nào trong table!")
            return
        
        print()
        print("=" * 50)
        print("📈 THỐNG KÊ DỮ LIỆU")
        print("=" * 50)
        
        # Lấy toàn bộ dữ liệu để phân tích
        df = table.to_pandas()
        
        # Hiển thị thông tin cột
        print(f"📋 Số cột: {len(df.columns)}")
        print(f"📝 Tên các cột: {list(df.columns)}")
        print()
        
        # Thống kê metadata
        if 'file_name' in df.columns:
            unique_files = df['file_name'].nunique()
            print(f"📄 Số file PDF unique: {unique_files}")
            print(f"📃 Danh sách files:")
            for file_name in df['file_name'].unique():
                count = len(df[df['file_name'] == file_name])
                print(f"   - {file_name}: {count} chunks")
        
        if 'chunk_length' in df.columns:
            avg_length = df['chunk_length'].mean()
            min_length = df['chunk_length'].min()
            max_length = df['chunk_length'].max()
            print(f"📏 Độ dài chunk trung bình: {avg_length:.0f} ký tự")
            print(f"📐 Độ dài chunk min/max: {min_length}/{max_length} ký tự")
        
        print()
        print("=" * 50)
        print("📄 MẪU DOCUMENTS")
        print("=" * 50)
        
        # Hiển thị 3 document đầu tiên
        sample_limit = min(3, total_rows)
        
        for i in range(sample_limit):
            row = df.iloc[i]
            print(f"\n📝 Document {i+1}:")
            print(f"   🔖 File: {row.get('file_name', 'N/A')}")
            print(f"   📄 Chunk: {row.get('chunk_index', 'N/A')}/{row.get('total_chunks', 'N/A')}")
            print(f"   📏 Độ dài: {row.get('chunk_length', 'N/A')} ký tự")
            print(f"   📃 Preview content:")
            
            content = row.get('text', '') or row.get('page_content', '')
            preview = content[:200] + "..." if len(content) > 200 else content
            print(f"      {preview}")
        
        print()
        print("=" * 50)
        print("🔍 SEARCH TEST")
        print("=" * 50)
        
        # Test search function với embedding
        try:
            print("🤖 Đang khởi tạo embedding model...")
            embeddings = OllamaEmbeddings(model="nomic-embed-text:latest")
            
            # Tạo vectorstore
            vectorstore = LanceDB(
                uri=str(lancedb_path),
                embedding=embeddings,
                table_name=table_name,
                mode="read"
            )
            
            # Test search
            test_query = "user calibration"
            print(f"🔍 Test search với query: '{test_query}'")
            
            results = vectorstore.similarity_search(test_query, k=10)
            
            print(f"✅ Tìm thấy {len(results)} kết quả:")
            for idx, doc in enumerate(results, 1):
                preview = doc.page_content[:150] + "..." if len(doc.page_content) > 150 else doc.page_content
                print(f"   {idx}. {preview}")
                print(f"      📄 File: {doc.metadata.get('file_name', 'N/A')}")
                print(f"      📄 Page: {doc.metadata.get('page_number', 'N/A')}")
                print()
        
        except Exception as e:
            print(f"⚠️ Không thể test search: {e}")
        
        print("=" * 50)
        print("✅ Hoàn thành xem knowledge base!")
        
    except Exception as e:
        print(f"❌ Lỗi khi truy cập LanceDB: {e}")
        return


if __name__ == "__main__":
    main() 