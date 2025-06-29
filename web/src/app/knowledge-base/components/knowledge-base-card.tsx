// Copyright (c) 2025 Bytedance Ltd. and/or its affiliates
// SPDX-License-Identifier: MIT

"use client";

import { useEffect, useState } from "react";
import { Database, FileText, Upload, Trash2, Edit3 } from "lucide-react";
import { toast } from "sonner";
import { useKnowledgeBaseStore } from "~/core/store/knowledge-base-store";
import { Button } from "~/components/ui/button";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "~/components/ui/card";
import { Badge } from "~/components/ui/badge";
import { EditKnowledgeBaseDialog } from "./edit-knowledge-base-dialog";

interface KnowledgeBaseCardProps {
  knowledgeBase: any;
  onRefresh: () => void;
}

export function KnowledgeBaseCard({ knowledgeBase, onRefresh }: KnowledgeBaseCardProps) {
  const [showDocuments, setShowDocuments] = useState(false);
  const [selectedFiles, setSelectedFiles] = useState<FileList | null>(null);
  const {
    fetchDocuments,
    getDocumentsByKnowledgeBaseId,
    uploadDocument,
    deleteDocument,
    deleteKnowledgeBase
  } = useKnowledgeBaseStore();

  const documents = getDocumentsByKnowledgeBaseId(knowledgeBase.id);

  useEffect(() => {
    if (showDocuments) {
      fetchDocuments(knowledgeBase.id);
    }
  }, [showDocuments, knowledgeBase.id, fetchDocuments]);

  const handleFileUpload = async (files: FileList) => {
    // Auto-open documents view to show the uploaded files
    if (!showDocuments) {
      setShowDocuments(true);
    }

    // Convert FileList to Array for easier processing
    const fileArray = Array.from(files);
    
    // Show initial toast for multiple files
    if (fileArray.length > 1) {
      toast.info(`Đang upload ${fileArray.length} tài liệu...`);
    }

    // Upload all files in parallel using Promise.allSettled
    const uploadPromises = fileArray.map(file => 
      uploadDocument(knowledgeBase.id, file)
    );

    try {
      const results = await Promise.allSettled(uploadPromises);
      
      // Count successes and failures
      let successCount = 0;
      let failureCount = 0;
      
      results.forEach((result, index) => {
        if (result.status === "fulfilled") {
          successCount++;
        } else {
          failureCount++;
          const fileName = fileArray[index]?.name || `file-${index}`;
          console.error(`Failed to upload ${fileName}:`, result.reason);
        }
      });

      // Show summary toast for multiple files
      if (fileArray.length > 1) {
        if (failureCount === 0) {
          toast.success(`Đã upload thành công tất cả ${successCount} tài liệu!`);
        } else if (successCount === 0) {
          toast.error(`Không thể upload tất cả ${failureCount} tài liệu.`);
        } else {
          toast.warning(`Upload hoàn thành: ${successCount} thành công, ${failureCount} thất bại.`);
        }
      }
      // Individual file toasts are handled in uploadDocument function
      
    } catch (error) {
      console.error("Unexpected error during batch upload:", error);
      toast.error("Có lỗi không mong muốn khi upload tài liệu.");
    }

    setSelectedFiles(null);
  };

  const getStatusColor = (status: string) => {
    switch (status) {
      case 'ready': return 'bg-green-500';
      case 'processing': return 'bg-yellow-500';
      case 'pending': return 'bg-blue-500';
      case 'error': return 'bg-red-500';
      default: return 'bg-gray-500';
    }
  };

  const getStatusText = (status: string) => {
    switch (status) {
      case 'ready': return 'Ready';
      case 'processing': return 'Processing';
      case 'pending': return 'Pending';
      case 'error': return 'Error';
      default: return 'Unknown';
    }
  };

  return (
    <Card className="h-fit">
      <CardHeader className="pb-3">
        <div className="flex items-start justify-between gap-2">
          <div className="flex-1 min-w-0 pr-2">
            <CardTitle className="flex items-center text-sm sm:text-base">
              <Database className="w-4 h-4 mr-2 flex-shrink-0" />
              <span className="truncate leading-tight">{knowledgeBase.name}</span>
            </CardTitle>
            {knowledgeBase.description && (
              <CardDescription className="mt-1 text-xs sm:text-sm line-clamp-2">
                {knowledgeBase.description}
              </CardDescription>
            )}
          </div>
          <div className="flex items-center gap-1.5 flex-shrink-0">
            <EditKnowledgeBaseDialog
              knowledgeBase={knowledgeBase}
              onSuccess={onRefresh}
              trigger={
                <Button
                  variant="ghost"
                  size="sm"
                  className="h-7 w-7 p-0 hover:bg-blue-500/10"
                >
                  <Edit3 className="w-3.5 h-3.5" />
                </Button>
              }
            />
            <Button
              variant="ghost"
              size="sm"
              onClick={() => deleteKnowledgeBase(knowledgeBase.id)}
              className="h-7 w-7 p-0 hover:bg-destructive/10"
            >
              <Trash2 className="w-3.5 h-3.5" />
            </Button>
          </div>
        </div>
      </CardHeader>
      <CardContent className="pt-0">
        <div className="space-y-3">
          <div className="flex flex-col gap-2">
            <input
              type="file"
              multiple
              accept=".pdf,.doc,.docx,.txt,.md"
              onChange={(e) => e.target.files && handleFileUpload(e.target.files)}
              className="hidden"
              id={`upload-${knowledgeBase.id}`}
            />
            <label htmlFor={`upload-${knowledgeBase.id}`} className="block">
              <Button 
                variant="outline" 
                asChild 
                className="text-xs sm:text-sm h-8 w-full justify-start"
                size="sm"
              >
                <span>
                  <Upload className="w-3.5 h-3.5 mr-2" />
                  Upload Documents
                </span>
              </Button>
            </label>
            
            <Button
              variant="outline"
              onClick={() => setShowDocuments(!showDocuments)}
              className="text-xs sm:text-sm h-8 justify-start"
              size="sm"
            >
              <FileText className="w-3.5 h-3.5 mr-2" />
              {showDocuments ? "Hide Documents" : "View Documents"}
            </Button>
          </div>

          {showDocuments && (
            <div className="space-y-2 border-t pt-3">
              <div className="text-xs sm:text-sm font-medium text-muted-foreground">
                Documents ({documents.length})
              </div>
              {documents.length === 0 ? (
                <div className="text-center text-muted-foreground py-4 text-xs">
                  No documents yet
                </div>
              ) : (
                <div className="space-y-1.5 max-h-48 overflow-y-auto">
                  {documents.map((doc) => (
                    <div key={`${doc.id}-${doc.updated_at}`} className="flex items-center gap-2 p-2 border rounded text-xs">
                      <FileText className="w-3.5 h-3.5 flex-shrink-0 text-muted-foreground" />
                      <div className="min-w-0 flex-1">
                        <div className="font-medium truncate">{doc.name}</div>
                        <div className="text-xs text-muted-foreground truncate">
                          {(doc.file_size / 1024).toFixed(1)} KB • {new Date(doc.created_at).toLocaleDateString('en-US')}
                        </div>
                      </div>
                      <div className="flex items-center gap-1.5 flex-shrink-0">
                        <Badge 
                          variant="outline" 
                          className={`text-xs px-1.5 py-0.5 ${getStatusColor(doc.status)}`}
                        >
                          {getStatusText(doc.status)}
                        </Badge>
                        <Button
                          variant="ghost"
                          size="sm"
                          onClick={() => deleteDocument(knowledgeBase.id, doc.id)}
                          className="h-6 w-6 p-0 hover:bg-destructive/10"
                        >
                          <Trash2 className="w-3 h-3" />
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