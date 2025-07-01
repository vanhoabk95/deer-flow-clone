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

  // Knowledge Base actions
  fetchKnowledgeBases: async () => {
    set({ loading: true });
    try {
      const knowledgeBases = await listKnowledgeBases();
      set({ knowledgeBases });
    } catch (error) {
      console.error("Failed to fetch knowledge bases:", error);
      toast.error("Unable to load knowledge bases");
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
      toast.success("Knowledge base created successfully");
      return newKnowledgeBase;
    } catch (error) {
      console.error("Failed to create knowledge base:", error);
      toast.error("Unable to create knowledge base");
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
      toast.success("Knowledge base updated successfully");
    } catch (error) {
      console.error("Failed to update knowledge base:", error);
      toast.error("Unable to update knowledge base");
    }
  },

  deleteKnowledgeBase: async (id: string) => {
    try {
      await deleteKnowledgeBase(id);
      set((state) => ({
        knowledgeBases: state.knowledgeBases.filter(kb => kb.id !== id),
        documents: new Map([...state.documents].filter(([kbId]) => kbId !== id))
      }));
      toast.success("Knowledge base deleted successfully");
    } catch (error) {
      console.error("Failed to delete knowledge base:", error);
      toast.error("Unable to delete knowledge base");
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
      toast.error("Unable to load documents");
    }
  },

  uploadDocument: async (knowledgeBaseId: string, file: File) => {
    try {
      // Validate file size (6MB limit)
      const maxSize = 6 * 1024 * 1024; // 6MB in bytes
      if (file.size > maxSize) {
        toast.error(`Document '${file.name}' is too large. Maximum allowed size is 6MB.`);
        return;
      }

      const document = await uploadDocument({ knowledge_base_id: knowledgeBaseId, file });

      // Update documents list with the returned document
      const currentDocuments = get().documents.get(knowledgeBaseId) || [];
      set((state) => ({
        documents: new Map(state.documents).set(knowledgeBaseId, [...currentDocuments, document])
      }));

      toast.success(`Successfully uploaded document '${file.name}'`);

      // Start polling for processing status immediately
      get().pollDocumentStatus(knowledgeBaseId, document.id);
    } catch (error: any) {
      console.error("Failed to upload document:", error);
      
      // Handle specific error cases
      if (error.message && error.message.includes("409:")) {
        // Extract detailed message from server response
        const serverMessage = error.message.split("409:")[1]?.trim();
        if (serverMessage && serverMessage.includes("Document")) {
          toast.error(serverMessage);
        } else {
          toast.error(`Document '${file.name}' already exists in this knowledge base. Please rename the file or delete the old document.`);
        }
      } else {
        toast.error(`Unable to upload document '${file.name}'. Please try again.`);
      }
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
      toast.success("Document deleted successfully");
    } catch (error) {
      console.error("Failed to delete document:", error);
      toast.error("Unable to delete document. Please try again.");
    }
  },

  pollDocumentStatus: async (knowledgeBaseId: string, documentId: string) => {
    const pollInterval = 500; // 500ms - faster polling for better UX
    const maxPolls = 120; // Max 1 minute (120 * 500ms)
    let pollCount = 0;

    const poll = async () => {
      try {
        const document = await getDocumentStatus(knowledgeBaseId, documentId);
        
        // Update document in store
        const currentDocuments = get().documents.get(knowledgeBaseId) || [];
        const docIndex = currentDocuments.findIndex(doc => doc.id === documentId);
        
        if (docIndex !== -1) {
          // Update existing document
          const updatedDocuments = [...currentDocuments];
          updatedDocuments[docIndex] = document;
          
          set((state) => ({
            documents: new Map(state.documents).set(knowledgeBaseId, updatedDocuments)
          }));
        } else {
          // Add new document if not found
          set((state) => ({
            documents: new Map(state.documents).set(knowledgeBaseId, [...currentDocuments, document])
          }));
        }

        // Check final status
        if (document.status === 'ready') {
          toast.success(`Document '${document.name}' has been processed and indexed successfully`);
          return;
        } else if (document.status === 'error') {
          toast.error(`Error processing document '${document.name}': ${document.error_message}`);
          return;
        }

        // Continue polling for any non-final status
        if (['pending', 'processing'].includes(document.status) && pollCount < maxPolls) {
          pollCount++;
          setTimeout(poll, pollInterval);
        } else if (pollCount >= maxPolls) {
          toast.warning(`Document '${document.name}' is taking longer than expected to process. Please check again later.`);
        }
      } catch (error) {
        console.error("Failed to poll document status:", error);
        // Stop polling on error
      }
    };

    // Start polling immediately
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