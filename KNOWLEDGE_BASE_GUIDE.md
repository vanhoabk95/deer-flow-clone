# Hướng dẫn sử dụng Knowledge Base trong DeerFlow

## Tổng quan

Tính năng Knowledge Base trong DeerFlow cho phép bạn:

- ✅ Tạo và quản lý knowledge base
- ✅ Tải lên tài liệu vào knowledge base
- ✅ Mention knowledge base trong chat để thực hiện RAG
- ✅ Xem trạng thái indexing của tài liệu
- ✅ Tìm kiếm knowledge base

## Cách sử dụng

### 1. Truy cập Knowledge Base

- Từ trang chủ: Click vào button "Knowledge Base"
- Từ trang chat: Click vào "Knowledge Base" trong header

### 2. Tạo Knowledge Base mới

1. Click vào button "Tạo Knowledge Base"
2. Nhập tên và mô tả (tùy chọn)
3. Click "Tạo"

### 3. Tải lên tài liệu

1. Trong knowledge base card, click "Tải lên tài liệu"
2. Chọn một hoặc nhiều file (hỗ trợ: .pdf, .doc, .docx, .txt, .md)
3. File sẽ được tải lên và tự động index

### 4. Sử dụng trong Chat

1. Mở trang chat
2. Khi nhập tin nhắn, gõ `@` để mention knowledge base
3. Chọn knowledge base từ danh sách gợi ý
4. Gửi tin nhắn để thực hiện RAG search

### 5. Quản lý Knowledge Base

- **Xem tài liệu**: Click "Xem tài liệu" để hiển thị danh sách
- **Xóa tài liệu**: Click icon thùng rác bên cạnh tài liệu
- **Xóa knowledge base**: Click icon thùng rác trên card

## Trạng thái tài liệu

- 🔵 **Đang tải lên**: File đang được upload
- 🟡 **Đang index**: File đang được xử lý và index
- 🟢 **Sẵn sàng**: File đã sẵn sàng để sử dụng
- 🔴 **Lỗi**: Có lỗi xảy ra trong quá trình xử lý

## API Endpoints

Hệ thống cung cấp các REST API endpoints:

```
GET    /api/knowledge-bases              # Lấy danh sách KB
POST   /api/knowledge-bases              # Tạo KB mới
PUT    /api/knowledge-bases/{id}         # Cập nhật KB
DELETE /api/knowledge-bases/{id}         # Xóa KB
GET    /api/knowledge-bases/search       # Tìm kiếm KB
GET    /api/knowledge-bases/{id}/documents     # Lấy tài liệu
POST   /api/knowledge-bases/{id}/documents     # Tải lên tài liệu
DELETE /api/knowledge-bases/{id}/documents/{doc_id}  # Xóa tài liệu
```

## Lưu ý

- Hiện tại đây là implementation đơn giản trong memory cho demo
- Dữ liệu sẽ mất khi restart server
- Để production, cần implement với database thực (PostgreSQL, MongoDB, etc.)
- Cần thêm vector store thực (Pinecone, Chroma, etc.) cho RAG search

## Tương lai

Các tính năng sẽ được phát triển:

- [ ] Persistent storage với database
- [ ] Vector embeddings và similarity search
- [ ] OCR cho file ảnh và PDF
- [ ] Chunk strategy tùy chỉnh
- [ ] Permission và sharing
- [ ] Analytics và usage tracking 