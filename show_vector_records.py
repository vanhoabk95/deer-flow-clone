#!/usr/bin/env python3
"""
Script để hiển thị tất cả các bản ghi trong vector database
"""

import os
import sys
from pathlib import Path

def show_all_vector_records():
    """Hiển thị tất cả các bản ghi trong vector database"""
    print("🔍 Vector Database Records Viewer")
    print("=" * 50)
    
    try:
        import lancedb
        print("✅ LanceDB import OK")
        
        # Kiểm tra thư mục appdata
        appdata_path = os.path.join(os.getcwd(), "appdata")
        print(f"📁 Appdata path: {appdata_path}")
        
        if not os.path.exists(appdata_path):
            print("❌ Appdata directory not found")
            return
        
        # Liệt kê các thư mục trong appdata
        kb_dirs = [d for d in os.listdir(appdata_path) 
                  if os.path.isdir(os.path.join(appdata_path, d))]
        
        print(f"📋 Found knowledge base directories: {kb_dirs}")
        
        if not kb_dirs:
            print("❌ No knowledge base directories found")
            return
        
        # Xử lý từng knowledge base
        for kb_id in kb_dirs:
            print(f"\n{'='*60}")
            print(f"🎯 KNOWLEDGE BASE: {kb_id}")
            print(f"{'='*60}")
            
            kb_path = os.path.join(appdata_path, kb_id)
            lancedb_path = os.path.join(kb_path, "lancedb")
            
            print(f"📁 KB path: {kb_path}")
            print(f"📁 LanceDB path: {lancedb_path}")
            
            if not os.path.exists(lancedb_path):
                print("❌ LanceDB directory not found")
                continue
            
            # Kết nối đến LanceDB
            db = lancedb.connect(lancedb_path)
            tables = db.table_names()
            print(f"📊 Tables: {tables}")
            
            if "documents" not in tables:
                print("❌ 'documents' table not found")
                continue
            
            # Mở table documents
            table = db.open_table("documents")
            
            # Lấy schema
            schema = table.schema
            print(f"\n📋 Schema:")
            for field in schema:
                print(f"  - {field.name}: {field.type}")
            
            # Đếm records
            count = table.count_rows()
            print(f"\n📊 Total records: {count}")
            
            if count == 0:
                print("ℹ️  No records found")
                continue
            
            # Lấy tất cả records
            df = table.to_pandas()
            
            # Nhóm theo file
            files = {}
            for _, row in df.iterrows():
                metadata = row.get('metadata', {})
                file_name = metadata.get('file_name', 'Unknown')
                
                if file_name not in files:
                    files[file_name] = []
                files[file_name].append(row)
            
            # Hiển thị từng file
            for file_name, records in files.items():
                print(f"\n📄 FILE: {file_name}")
                print(f"   Chunks: {len(records)}")
                print(f"   {'-'*40}")
                
                # Sắp xếp theo chunk_index
                records.sort(key=lambda x: x.get('metadata', {}).get('chunk_index', 0))
                
                for i, record in enumerate(records):
                    metadata = record.get('metadata', {})
                    chunk_index = metadata.get('chunk_index', 'N/A')
                    total_chunks = metadata.get('total_chunks', 'N/A')
                    chunk_length = metadata.get('chunk_length', 'N/A')
                    
                    print(f"\n   Chunk {chunk_index}/{total_chunks} (Length: {chunk_length} chars):")
                    
                    # Hiển thị text
                    text = record.get('text', '')
                    if text:
                        # Loại bỏ các ký tự xuống dòng và khoảng trắng thừa
                        cleaned_text = ' '.join(text.split())
                        if len(cleaned_text) > 200:
                            preview = cleaned_text[:200] + "..."
                        else:
                            preview = cleaned_text
                        print(f"   Content: {preview}")
                    
                    # Hiển thị ID
                    record_id = record.get('id', 'N/A')
                    print(f"   ID: {record_id}")
            
            # Test search với một số từ khóa
            print(f"\n🔍 Search Test Results:")
            test_queries = ["test", "phân phối", "chuẩn", "data"]
            
            for query in test_queries:
                try:
                    # Tạo query vector đơn giản (zeros)
                    import numpy as np
                    query_vector = np.zeros(768)
                    
                    # Thực hiện search
                    results = table.search(query_vector).limit(2).to_pandas()
                    
                    if not results.empty:
                        print(f"   Query '{query}': Found {len(results)} results")
                        for idx, row in results.head(1).iterrows():
                            metadata = row.get('metadata', {})
                            file_name = metadata.get('file_name', 'N/A')
                            score = row.get('_distance', 'N/A')
                            print(f"     - File: {file_name}, Score: {score:.4f}")
                    else:
                        print(f"   Query '{query}': No results")
                        
                except Exception as e:
                    print(f"   Query '{query}': Error - {e}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return False

def show_specific_file_records(kb_id: str, file_name: str):
    """Hiển thị records của một file cụ thể"""
    print(f"\n🔍 Records for file: {file_name} in KB: {kb_id}")
    print("=" * 60)
    
    try:
        import lancedb
        
        appdata_path = os.path.join(os.getcwd(), "appdata")
        kb_path = os.path.join(appdata_path, kb_id)
        lancedb_path = os.path.join(kb_path, "lancedb")
        
        if not os.path.exists(lancedb_path):
            print("❌ LanceDB directory not found")
            return
        
        # Kết nối đến LanceDB
        db = lancedb.connect(lancedb_path)
        table = db.open_table("documents")
        
        # Lấy tất cả records
        df = table.to_pandas()
        
        # Lọc records cho file cụ thể
        file_records = []
        for _, row in df.iterrows():
            metadata = row.get('metadata', {})
            if metadata.get('file_name') == file_name:
                file_records.append(row)
        
        if not file_records:
            print(f"❌ No records found for file: {file_name}")
            return
        
        print(f"📄 Found {len(file_records)} chunks for file: {file_name}")
        
        # Sắp xếp theo chunk_index
        file_records.sort(key=lambda x: x.get('metadata', {}).get('chunk_index', 0))
        
        for i, record in enumerate(file_records):
            metadata = record.get('metadata', {})
            chunk_index = metadata.get('chunk_index', 'N/A')
            total_chunks = metadata.get('total_chunks', 'N/A')
            chunk_length = metadata.get('chunk_length', 'N/A')
            
            print(f"\n📝 Chunk {chunk_index}/{total_chunks} (Length: {chunk_length} chars):")
            print(f"   ID: {record.get('id', 'N/A')}")
            
            # Hiển thị toàn bộ text
            text = record.get('text', '')
            if text:
                print(f"   Content:")
                print(f"   {text}")
            
            print(f"   {'-'*50}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """Main function"""
    print("🚀 Vector Database Records Viewer")
    print("=" * 50)
    
    # Hiển thị tất cả records
    show_all_vector_records()
    
    # Hiển thị records của file cụ thể (nếu có)
    print(f"\n{'='*60}")
    print("📄 DETAILED FILE VIEW")
    print(f"{'='*60}")
    
    # Tìm file đầu tiên để hiển thị chi tiết
    try:
        import lancedb
        appdata_path = os.path.join(os.getcwd(), "appdata")
        kb_dirs = [d for d in os.listdir(appdata_path) 
                  if os.path.isdir(os.path.join(appdata_path, d))]
        
        if kb_dirs:
            kb_id = kb_dirs[0]
            kb_path = os.path.join(appdata_path, kb_id)
            lancedb_path = os.path.join(kb_path, "lancedb")
            
            if os.path.exists(lancedb_path):
                db = lancedb.connect(lancedb_path)
                table = db.open_table("documents")
                df = table.to_pandas()
                
                # Tìm file đầu tiên
                for _, row in df.iterrows():
                    metadata = row.get('metadata', {})
                    file_name = metadata.get('file_name', '')
                    if file_name:
                        show_specific_file_records(kb_id, file_name)
                        break
    
    except Exception as e:
        print(f"⚠️  Detailed view failed: {e}")
    
    print("\n🎉 Script completed!")

if __name__ == "__main__":
    main() 