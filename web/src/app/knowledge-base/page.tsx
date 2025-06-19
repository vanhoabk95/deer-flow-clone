// Copyright (c) 2025 Bytedance Ltd. and/or its affiliates
// SPDX-License-Identifier: MIT

"use client";

import { useEffect, useState } from "react";
import { Plus, Database, FileText, Upload, Trash2, Edit3, Search } from "lucide-react";
import { useKnowledgeBaseStore } from "~/core/store/knowledge-base-store";
import { Button } from "~/components/ui/button";
import { Input } from "~/components/ui/input";
import { Textarea } from "~/components/ui/textarea";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "~/components/ui/card";
import { Dialog, DialogContent, DialogDescription, DialogHeader, DialogTitle, DialogTrigger } from "~/components/ui/dialog";
import { Badge } from "~/components/ui/badge";
import { Skeleton } from "~/components/ui/skeleton";
import { Separator } from "~/components/ui/separator";

interface CreateKnowledgeBaseDialogProps {
  onSuccess?: () => void;
}

function CreateKnowledgeBaseDialog({ onSuccess }: CreateKnowledgeBaseDialogProps) {
  const [open, setOpen] = useState(false);
  const [name, setName] = useState("");
  const [description, setDescription] = useState("");
  const [loading, setLoading] = useState(false);
  const { createKnowledgeBase } = useKnowledgeBaseStore();

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!name.trim()) return;

    setLoading(true);
    const result = await createKnowledgeBase(name.trim(), description.trim() || undefined);
    setLoading(false);

    if (result) {
      setName("");
      setDescription("");
      setOpen(false);
      onSuccess?.();
    }
  };

  return (
    <Dialog open={open} onOpenChange={setOpen}>
      <DialogTrigger asChild>
        <Button>
          <Plus className="w-4 h-4 mr-2" />
          Tạo Knowledge Base
        </Button>
      </DialogTrigger>
      <DialogContent>
        <DialogHeader>
          <DialogTitle>Tạo Knowledge Base mới</DialogTitle>
          <DialogDescription>
            Tạo một knowledge base để lưu trữ và quản lý tài liệu của bạn.
          </DialogDescription>
        </DialogHeader>
        <form onSubmit={handleSubmit} className="space-y-4">
          <div>
            <label htmlFor="name" className="text-sm font-medium">
              Tên Knowledge Base *
            </label>
            <Input
              id="name"
              value={name}
              onChange={(e) => setName(e.target.value)}
              placeholder="Nhập tên knowledge base"
              required
            />
          </div>
          <div>
            <label htmlFor="description" className="text-sm font-medium">
              Mô tả
            </label>
            <Textarea
              id="description"
              value={description}
              onChange={(e) => setDescription(e.target.value)}
              placeholder="Nhập mô tả cho knowledge base"
              rows={3}
            />
          </div>
          <div className="flex justify-end space-x-2">
            <Button type="button" variant="outline" onClick={() => setOpen(false)}>
              Hủy
            </Button>
            <Button type="submit" disabled={loading || !name.trim()}>
              {loading ? "Đang tạo..." : "Tạo"}
            </Button>
          </div>
        </form>
      </DialogContent>
    </Dialog>
  );
}

function KnowledgeBaseCard({ knowledgeBase }: { knowledgeBase: any }) {
  const [showDocuments, setShowDocuments] = useState(false);
  const [selectedFiles, setSelectedFiles] = useState<FileList | null>(null);
  const {
    fetchDocuments,
    getDocumentsByKnowledgeBaseId,
    uploadDocument,
    deleteDocument,
    deleteKnowledgeBase,
    uploadingFiles
  } = useKnowledgeBaseStore();

  const documents = getDocumentsByKnowledgeBaseId(knowledgeBase.id);

  useEffect(() => {
    if (showDocuments) {
      fetchDocuments(knowledgeBase.id);
    }
  }, [showDocuments, knowledgeBase.id, fetchDocuments]);

  const handleFileUpload = async (files: FileList) => {
    for (let i = 0; i < files.length; i++) {
      const file = files.item(i);
      if (file) {
        await uploadDocument(knowledgeBase.id, file);
      }
    }
    setSelectedFiles(null);
  };

  const getStatusColor = (status: string) => {
    switch (status) {
      case 'ready': return 'bg-green-500';
      case 'indexing': return 'bg-yellow-500';
      case 'uploading': return 'bg-blue-500';
      case 'error': return 'bg-red-500';
      default: return 'bg-gray-500';
    }
  };

  const getStatusText = (status: string) => {
    switch (status) {
      case 'ready': return 'Sẵn sàng';
      case 'indexing': return 'Đang index';
      case 'uploading': return 'Đang tải lên';
      case 'error': return 'Lỗi';
      default: return 'Không xác định';
    }
  };

  return (
    <Card>
      <CardHeader>
        <div className="flex items-start justify-between">
          <div>
            <CardTitle className="flex items-center">
              <Database className="w-5 h-5 mr-2" />
              {knowledgeBase.name}
            </CardTitle>
            {knowledgeBase.description && (
              <CardDescription className="mt-1">
                {knowledgeBase.description}
              </CardDescription>
            )}
          </div>
          <div className="flex items-center space-x-2">
            <Badge variant="secondary">
              {knowledgeBase.document_count} tài liệu
            </Badge>
            <Button
              variant="ghost"
              size="sm"
              onClick={() => deleteKnowledgeBase(knowledgeBase.id)}
            >
              <Trash2 className="w-4 h-4" />
            </Button>
          </div>
        </div>
      </CardHeader>
      <CardContent>
        <div className="space-y-4">
          <div className="flex items-center justify-between">
            <Button
              variant="outline"
              onClick={() => setShowDocuments(!showDocuments)}
            >
              <FileText className="w-4 h-4 mr-2" />
              {showDocuments ? "Ẩn tài liệu" : "Xem tài liệu"}
            </Button>
            <div>
              <input
                type="file"
                multiple
                accept=".pdf,.doc,.docx,.txt,.md"
                onChange={(e) => e.target.files && handleFileUpload(e.target.files)}
                className="hidden"
                id={`upload-${knowledgeBase.id}`}
              />
              <label htmlFor={`upload-${knowledgeBase.id}`}>
                <Button variant="outline" asChild>
                  <span>
                    <Upload className="w-4 h-4 mr-2" />
                    Tải lên tài liệu
                  </span>
                </Button>
              </label>
            </div>
          </div>

          {/* Show uploading files */}
          {Array.from(uploadingFiles.entries()).map(([fileId, fileInfo]) => {
            if (!fileId.startsWith(knowledgeBase.id)) return null;
            return (
              <div key={fileId} className="flex items-center space-x-2 p-2 bg-blue-50 rounded">
                <Upload className="w-4 h-4 text-blue-500" />
                <span className="flex-1 text-sm">{fileInfo.fileName}</span>
                <Badge variant="outline">Đang tải lên</Badge>
              </div>
            );
          })}

          {showDocuments && (
            <div className="space-y-2">
              <Separator />
              <div className="text-sm font-medium">Tài liệu ({documents.length})</div>
              {documents.length === 0 ? (
                <div className="text-center text-gray-500 py-4">
                  Chưa có tài liệu nào
                </div>
              ) : (
                <div className="space-y-2">
                  {documents.map((doc) => (
                    <div key={doc.id} className="flex items-center justify-between p-2 border rounded">
                      <div className="flex items-center space-x-2">
                        <FileText className="w-4 h-4" />
                        <div>
                          <div className="text-sm font-medium">{doc.name}</div>
                          <div className="text-xs text-gray-500">
                            {(doc.file_size / 1024).toFixed(1)} KB • {new Date(doc.created_at).toLocaleDateString('vi-VN')}
                          </div>
                        </div>
                      </div>
                      <div className="flex items-center space-x-2">
                        <Badge variant="outline" className={getStatusColor(doc.status)}>
                          {getStatusText(doc.status)}
                        </Badge>
                        <Button
                          variant="ghost"
                          size="sm"
                          onClick={() => deleteDocument(knowledgeBase.id, doc.id)}
                        >
                          <Trash2 className="w-4 h-4" />
                        </Button>
                      </div>
                    </div>
                  ))}
                </div>
              )}
            </div>
          )}
        </div>
      </CardContent>
    </Card>
  );
}

export default function KnowledgeBasePage() {
  const [searchQuery, setSearchQuery] = useState("");
  const { knowledgeBases, loading, fetchKnowledgeBases } = useKnowledgeBaseStore();

  useEffect(() => {
    fetchKnowledgeBases();
  }, [fetchKnowledgeBases]);

  const filteredKnowledgeBases = knowledgeBases.filter(kb =>
    kb.name.toLowerCase().includes(searchQuery.toLowerCase()) ||
    (kb.description && kb.description.toLowerCase().includes(searchQuery.toLowerCase()))
  );

  return (
    <div className="container mx-auto py-8 px-4">
      <div className="flex items-center justify-between mb-8">
        <div>
          <h1 className="text-3xl font-bold">Knowledge Base</h1>
          <p className="text-gray-600 mt-2">
            Quản lý các knowledge base và tài liệu của bạn
          </p>
        </div>
        <CreateKnowledgeBaseDialog onSuccess={fetchKnowledgeBases} />
      </div>

      <div className="flex items-center space-x-4 mb-6">
        <div className="relative flex-1 max-w-md">
          <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400 w-4 h-4" />
          <Input
            placeholder="Tìm kiếm knowledge base..."
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            className="pl-10"
          />
        </div>
      </div>

      {loading ? (
        <div className="grid gap-6 md:grid-cols-2 lg:grid-cols-3">
          {[1, 2, 3].map((i) => (
            <Card key={i}>
              <CardHeader>
                <Skeleton className="h-6 w-3/4" />
                <Skeleton className="h-4 w-full" />
              </CardHeader>
              <CardContent>
                <Skeleton className="h-20 w-full" />
              </CardContent>
            </Card>
          ))}
        </div>
      ) : filteredKnowledgeBases.length === 0 ? (
        <div className="text-center py-12">
          <Database className="w-16 h-16 text-gray-400 mx-auto mb-4" />
          <h3 className="text-lg font-medium text-gray-900 mb-2">
            {searchQuery ? "Không tìm thấy knowledge base" : "Chưa có knowledge base nào"}
          </h3>
          <p className="text-gray-500 mb-4">
            {searchQuery 
              ? "Thử thay đổi từ khóa tìm kiếm của bạn"
              : "Bắt đầu bằng cách tạo knowledge base đầu tiên"
            }
          </p>
          {!searchQuery && <CreateKnowledgeBaseDialog onSuccess={fetchKnowledgeBases} />}
        </div>
      ) : (
        <div className="grid gap-6 md:grid-cols-2 lg:grid-cols-3">
          {filteredKnowledgeBases.map((knowledgeBase) => (
            <KnowledgeBaseCard
              key={knowledgeBase.id}
              knowledgeBase={knowledgeBase}
            />
          ))}
        </div>
      )}
    </div>
  );
} 