// Copyright (c) 2025 Bytedance Ltd. and/or its affiliates
// SPDX-License-Identifier: MIT

"use client";

import { useEffect, useState } from "react";
import { Plus, Database, FileText, Upload, Trash2, Edit3, MessageSquare } from "lucide-react";
import { useKnowledgeBaseStore } from "~/core/store/knowledge-base-store";
import { Button } from "~/components/ui/button";
import { Input } from "~/components/ui/input";
import { Textarea } from "~/components/ui/textarea";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "~/components/ui/card";
import { Dialog, DialogContent, DialogDescription, DialogHeader, DialogTitle, DialogTrigger } from "~/components/ui/dialog";
import { Badge } from "~/components/ui/badge";
import { Skeleton } from "~/components/ui/skeleton";
import { Separator } from "~/components/ui/separator";
import { Logo } from "~/components/deer-flow/logo";
import { ThemeToggle } from "~/components/deer-flow/theme-toggle";
import { SettingsDialog } from "../settings/dialogs/settings-dialog";
import Link from "next/link";
import { Suspense } from "react";

interface CreateKnowledgeBaseDialogProps {
  onSuccess?: () => void;
}

interface EditKnowledgeBaseDialogProps {
  knowledgeBase: any;
  onSuccess?: () => void;
  trigger: React.ReactNode;
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
          Create Knowledge Base
        </Button>
      </DialogTrigger>
      <DialogContent>
        <DialogHeader>
          <DialogTitle>Create New Knowledge Base</DialogTitle>
          <DialogDescription>
            Create a knowledge base to store and manage your documents.
          </DialogDescription>
        </DialogHeader>
        <form onSubmit={handleSubmit} className="space-y-4">
          <div>
            <label htmlFor="name" className="text-sm font-medium">
              Knowledge Base Name *
            </label>
            <Input
              id="name"
              value={name}
              onChange={(e) => setName(e.target.value)}
              placeholder="Enter knowledge base name"
              required
            />
          </div>
          <div>
            <label htmlFor="description" className="text-sm font-medium">
              Description
            </label>
            <Textarea
              id="description"
              value={description}
              onChange={(e) => setDescription(e.target.value)}
              placeholder="Enter description for knowledge base"
              rows={3}
            />
          </div>
          <div className="flex justify-end space-x-2">
            <Button type="button" variant="outline" onClick={() => setOpen(false)}>
              Cancel
            </Button>
            <Button type="submit" disabled={loading || !name.trim()}>
              {loading ? "Creating..." : "Create"}
            </Button>
          </div>
        </form>
      </DialogContent>
    </Dialog>
  );
}

function EditKnowledgeBaseDialog({ knowledgeBase, onSuccess, trigger }: EditKnowledgeBaseDialogProps) {
  const [open, setOpen] = useState(false);
  const [name, setName] = useState(knowledgeBase.name);
  const [description, setDescription] = useState(knowledgeBase.description || "");
  const [loading, setLoading] = useState(false);
  const { updateKnowledgeBase } = useKnowledgeBaseStore();

  // Reset form when dialog opens
  const handleOpenChange = (newOpen: boolean) => {
    if (newOpen) {
      setName(knowledgeBase.name);
      setDescription(knowledgeBase.description || "");
    }
    setOpen(newOpen);
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!name.trim()) return;

    setLoading(true);
    await updateKnowledgeBase(knowledgeBase.id, name.trim(), description.trim() || undefined);
    setLoading(false);
    setOpen(false);
    onSuccess?.();
  };

  return (
    <Dialog open={open} onOpenChange={handleOpenChange}>
      <DialogTrigger asChild>
        {trigger}
      </DialogTrigger>
      <DialogContent>
        <DialogHeader>
          <DialogTitle>Edit Knowledge Base</DialogTitle>
          <DialogDescription>
            Update the name and description of your knowledge base.
          </DialogDescription>
        </DialogHeader>
        <form onSubmit={handleSubmit} className="space-y-4">
          <div>
            <label htmlFor="edit-name" className="text-sm font-medium">
              Knowledge Base Name *
            </label>
            <Input
              id="edit-name"
              value={name}
              onChange={(e) => setName(e.target.value)}
              placeholder="Enter knowledge base name"
              required
            />
          </div>
          <div>
            <label htmlFor="edit-description" className="text-sm font-medium">
              Description
            </label>
            <Textarea
              id="edit-description"
              value={description}
              onChange={(e) => setDescription(e.target.value)}
              placeholder="Enter description for knowledge base"
              rows={3}
            />
          </div>
          <div className="flex justify-end space-x-2">
            <Button type="button" variant="outline" onClick={() => setOpen(false)}>
              Cancel
            </Button>
            <Button type="submit" disabled={loading || !name.trim()}>
              {loading ? "Updating..." : "Update"}
            </Button>
          </div>
        </form>
      </DialogContent>
    </Dialog>
  );
}

function KnowledgeBaseCard({ knowledgeBase, onRefresh }: { knowledgeBase: any; onRefresh: () => void }) {
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
      case 'ready': return 'Ready';
      case 'indexing': return 'Indexing';
      case 'uploading': return 'Uploading';
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

          {/* Show uploading files */}
          {Array.from(uploadingFiles.entries()).map(([fileId, fileInfo]) => {
            if (!fileId.startsWith(knowledgeBase.id)) return null;
            return (
              <div key={fileId} className="flex items-center gap-2 p-2 bg-blue-50 dark:bg-blue-950/20 rounded text-xs">
                <Upload className="w-3.5 h-3.5 text-blue-500 flex-shrink-0" />
                <span className="flex-1 truncate">{fileInfo.fileName}</span>
                <Badge variant="outline" className="text-xs px-1.5 py-0.5">Uploading</Badge>
              </div>
            );
          })}

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
                    <div key={doc.id} className="flex items-center gap-2 p-2 border rounded text-xs">
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

export default function KnowledgeBasePage() {
  const { knowledgeBases, loading, fetchKnowledgeBases } = useKnowledgeBaseStore();

  useEffect(() => {
    fetchKnowledgeBases();
  }, [fetchKnowledgeBases]);

  return (
    <div className="flex h-screen w-screen flex-col overscroll-none">
      {/* Header */}
      <header className="flex h-12 w-full items-center justify-between px-3 sm:px-4 z-50 bg-background/80 backdrop-blur-sm border-b flex-shrink-0">
        <Logo />
        <div className="flex items-center space-x-2">
          <Link href="/chat">
            <Button variant="ghost" size="sm" className="text-xs sm:text-sm">
              <MessageSquare className="w-4 h-4 mr-1 sm:mr-2" />
              <span className="hidden sm:inline">Chat</span>
            </Button>
          </Link>
          <ThemeToggle />
          <Suspense>
            <SettingsDialog />
          </Suspense>
        </div>
      </header>

      {/* Main content */}
      <div className="flex-1 overflow-auto min-h-0">
        <div className="container mx-auto py-4 sm:py-8 px-3 sm:px-4 max-w-7xl min-h-full">
          <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 mb-6 sm:mb-8">
            <div className="min-w-0">
              <h1 className="text-2xl sm:text-3xl font-bold truncate">Knowledge Base</h1>
              <p className="text-gray-600 dark:text-gray-300 mt-1 sm:mt-2 text-sm sm:text-base">
                Manage your knowledge bases and documents
              </p>
            </div>
            <div className="flex-shrink-0">
              <CreateKnowledgeBaseDialog onSuccess={fetchKnowledgeBases} />
            </div>
          </div>

          {loading ? (
            <div className="grid gap-3 sm:gap-4 lg:gap-6 grid-cols-1 sm:grid-cols-2 lg:grid-cols-3">
              {[1, 2, 3].map((i) => (
                <Card key={i} className="h-fit">
                  <CardHeader className="pb-3">
                    <Skeleton className="h-5 w-3/4" />
                    <Skeleton className="h-3 w-full" />
                  </CardHeader>
                  <CardContent className="pt-0">
                    <Skeleton className="h-16 w-full" />
                  </CardContent>
                </Card>
              ))}
            </div>
          ) : knowledgeBases.length === 0 ? (
            <div className="text-center py-8 sm:py-12">
              <p className="text-gray-700 dark:text-gray-300 text-lg sm:text-xl font-semibold">
                Get started by creating your first knowledge base
              </p>
            </div>
          ) : (
            <div className="grid gap-3 sm:gap-4 lg:gap-6 grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 auto-rows-fr">
              {knowledgeBases.map((knowledgeBase) => (
                <div key={knowledgeBase.id} className="w-full max-w-full">
                  <KnowledgeBaseCard
                    knowledgeBase={knowledgeBase}
                    onRefresh={fetchKnowledgeBases}
                  />
                </div>
              ))}
            </div>
          )}
        </div>
      </div>
    </div>
  );
} 