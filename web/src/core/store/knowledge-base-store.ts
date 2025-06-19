// Copyright (c) 2025 Bytedance Ltd. and/or its affiliates
// SPDX-License-Identifier: MIT

import { create } from "zustand";
import { toast } from "sonner";
import type { KnowledgeBase, Document } from "../api/types";
import { 
  listKnowledgeBases, 
  createKnowledgeBase, 
  updateKnowledgeBase,
  deleteKnowledgeBase,
  listDocuments,
  uploadDocument,
  deleteDocument,
  getDocumentStatus 
} from "../api/knowledge-base";

interface KnowledgeBaseStore {
  // State
  knowledgeBases: KnowledgeBase[];
  documents: Map<string, Document[]>; // Map<knowledgeBaseId, Document[]>
  loading: boolean;
  uploadingFiles: Map<string, { fileName: string; progress: number }>; // Map<fileId, upload status>

  // Knowledge Base actions
  fetchKnowledgeBases: () => Promise<void>;
  createKnowledgeBase: (name: string, description?: string) => Promise<KnowledgeBase | null>;
  updateKnowledgeBase: (id: string, name: string, description?: string) => Promise<void>;
  deleteKnowledgeBase: (id: string) => Promise<void>;

  // Document actions
  fetchDocuments: (knowledgeBaseId: string) => Promise<void>;
  uploadDocument: (knowledgeBaseId: string, file: File) => Promise<void>;
  deleteDocument: (knowledgeBaseId: string, documentId: string) => Promise<void>;
  pollDocumentStatus: (knowledgeBaseId: string, documentId: string) => Promise<void>;

  // UI helpers
  getKnowledgeBaseById: (id: string) => KnowledgeBase | undefined;
  getDocumentsByKnowledgeBaseId: (knowledgeBaseId: string) => Document[];
}

export const useKnowledgeBaseStore = create<KnowledgeBaseStore>((set, get) => ({
  // Initial state
  knowledgeBases: [],
  documents: new Map(),
  loading: false,
  uploadingFiles: new Map(),

  // Knowledge Base actions
  fetchKnowledgeBases: async () => {
    set({ loading: true });
    try {
      const knowledgeBases = await listKnowledgeBases();
      set({ knowledgeBases });
    } catch (error) {
      console.error("Failed to fetch knowledge bases:", error);
      toast.error("Không thể tải danh sách knowledge base");
    } finally {
      set({ loading: false });
    }
  },

  createKnowledgeBase: async (name: string, description?: string) => {
    try {
      const newKnowledgeBase = await createKnowledgeBase({ name, description });
      set((state) => ({
        knowledgeBases: [...state.knowledgeBases, newKnowledgeBase]
      }));
      toast.success("Tạo knowledge base thành công");
      return newKnowledgeBase;
    } catch (error) {
      console.error("Failed to create knowledge base:", error);
      toast.error("Không thể tạo knowledge base");
      return null;
    }
  },

  updateKnowledgeBase: async (id: string, name: string, description?: string) => {
    try {
      const updatedKnowledgeBase = await updateKnowledgeBase(id, { name, description });
      set((state) => ({
        knowledgeBases: state.knowledgeBases.map(kb => 
          kb.id === id ? updatedKnowledgeBase : kb
        )
      }));
      toast.success("Cập nhật knowledge base thành công");
    } catch (error) {
      console.error("Failed to update knowledge base:", error);
      toast.error("Không thể cập nhật knowledge base");
    }
  },

  deleteKnowledgeBase: async (id: string) => {
    try {
      await deleteKnowledgeBase(id);
      set((state) => ({
        knowledgeBases: state.knowledgeBases.filter(kb => kb.id !== id),
        documents: new Map([...state.documents].filter(([kbId]) => kbId !== id))
      }));
      toast.success("Xóa knowledge base thành công");
    } catch (error) {
      console.error("Failed to delete knowledge base:", error);
      toast.error("Không thể xóa knowledge base");
    }
  },

  // Document actions
  fetchDocuments: async (knowledgeBaseId: string) => {
    try {
      const documents = await listDocuments(knowledgeBaseId);
      set((state) => ({
        documents: new Map(state.documents).set(knowledgeBaseId, documents)
      }));
    } catch (error) {
      console.error("Failed to fetch documents:", error);
      toast.error("Không thể tải danh sách tài liệu");
    }
  },

  uploadDocument: async (knowledgeBaseId: string, file: File) => {
    const fileId = `${knowledgeBaseId}-${file.name}-${Date.now()}`;
    
    // Add to uploading files
    set((state) => ({
      uploadingFiles: new Map(state.uploadingFiles).set(fileId, { 
        fileName: file.name, 
        progress: 0 
      })
    }));

    try {
      const document = await uploadDocument({ knowledge_base_id: knowledgeBaseId, file });
      
      // Update documents list
      const currentDocuments = get().documents.get(knowledgeBaseId) || [];
      set((state) => ({
        documents: new Map(state.documents).set(knowledgeBaseId, [...currentDocuments, document])
      }));

      // Remove from uploading files
      set((state) => {
        const newUploadingFiles = new Map(state.uploadingFiles);
        newUploadingFiles.delete(fileId);
        return { uploadingFiles: newUploadingFiles };
      });

      toast.success(`Tải lên ${file.name} thành công`);

      // Start polling for indexing status
      get().pollDocumentStatus(knowledgeBaseId, document.id);
    } catch (error) {
      console.error("Failed to upload document:", error);
      toast.error(`Không thể tải lên ${file.name}`);
      
      // Remove from uploading files
      set((state) => {
        const newUploadingFiles = new Map(state.uploadingFiles);
        newUploadingFiles.delete(fileId);
        return { uploadingFiles: newUploadingFiles };
      });
    }
  },

  deleteDocument: async (knowledgeBaseId: string, documentId: string) => {
    try {
      await deleteDocument(knowledgeBaseId, documentId);
      const currentDocuments = get().documents.get(knowledgeBaseId) || [];
      set((state) => ({
        documents: new Map(state.documents).set(
          knowledgeBaseId, 
          currentDocuments.filter(doc => doc.id !== documentId)
        )
      }));
      toast.success("Xóa tài liệu thành công");
    } catch (error) {
      console.error("Failed to delete document:", error);
      toast.error("Không thể xóa tài liệu");
    }
  },

  pollDocumentStatus: async (knowledgeBaseId: string, documentId: string) => {
    const pollInterval = 2000; // 2 seconds
    const maxPolls = 30; // Max 1 minute
    let pollCount = 0;

    const poll = async () => {
      try {
        const document = await getDocumentStatus(knowledgeBaseId, documentId);
        
        // Update document in store
        const currentDocuments = get().documents.get(knowledgeBaseId) || [];
        set((state) => ({
          documents: new Map(state.documents).set(
            knowledgeBaseId,
            currentDocuments.map(doc => doc.id === documentId ? document : doc)
          )
        }));

        if (document.status === 'ready') {
          toast.success(`Tài liệu ${document.name} đã được index thành công`);
          return;
        } else if (document.status === 'error') {
          toast.error(`Lỗi khi index tài liệu ${document.name}: ${document.error_message}`);
          return;
        }

        // Continue polling if still indexing
        if (document.status === 'indexing' && pollCount < maxPolls) {
          pollCount++;
          setTimeout(poll, pollInterval);
        }
      } catch (error) {
        console.error("Failed to poll document status:", error);
      }
    };

    poll();
  },

  // UI helpers
  getKnowledgeBaseById: (id: string) => {
    return get().knowledgeBases.find(kb => kb.id === id);
  },

  getDocumentsByKnowledgeBaseId: (knowledgeBaseId: string) => {
    return get().documents.get(knowledgeBaseId) || [];
  },
})); 