// Copyright (c) 2025 Bytedance Ltd. and/or its affiliates
// SPDX-License-Identifier: MIT

import { resolveServiceURL } from "./resolve-service-url";
import type { 
  KnowledgeBase, 
  Document, 
  CreateKnowledgeBaseRequest, 
  UploadDocumentRequest 
} from "./types";

// Knowledge Base API
export async function listKnowledgeBases(): Promise<KnowledgeBase[]> {
  const response = await fetch(resolveServiceURL("knowledge-bases"));
  if (!response.ok) {
    throw new Error(`Failed to fetch knowledge bases: ${response.statusText}`);
  }
  return response.json();
}

export async function createKnowledgeBase(
  data: CreateKnowledgeBaseRequest
): Promise<KnowledgeBase> {
  const response = await fetch(resolveServiceURL("knowledge-bases"), {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  });
  if (!response.ok) {
    throw new Error(`Failed to create knowledge base: ${response.statusText}`);
  }
  return response.json();
}

export async function updateKnowledgeBase(
  id: string,
  data: Partial<CreateKnowledgeBaseRequest>
): Promise<KnowledgeBase> {
  const response = await fetch(resolveServiceURL(`knowledge-bases/${id}`), {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  });
  if (!response.ok) {
    throw new Error(`Failed to update knowledge base: ${response.statusText}`);
  }
  return response.json();
}

export async function deleteKnowledgeBase(id: string): Promise<void> {
  const response = await fetch(resolveServiceURL(`knowledge-bases/${id}`), {
    method: "DELETE",
  });
  if (!response.ok) {
    throw new Error(`Failed to delete knowledge base: ${response.statusText}`);
  }
}

// Document API
export async function listDocuments(knowledgeBaseId: string): Promise<Document[]> {
  const response = await fetch(
    resolveServiceURL(`knowledge-bases/${knowledgeBaseId}/documents`)
  );
  if (!response.ok) {
    throw new Error(`Failed to fetch documents: ${response.statusText}`);
  }
  return response.json();
}

export async function uploadDocument(
  data: UploadDocumentRequest
): Promise<Document> {
  const formData = new FormData();
  formData.append("file", data.file);
  formData.append("knowledge_base_id", data.knowledge_base_id);

  const response = await fetch(
    resolveServiceURL(`knowledge-bases/${data.knowledge_base_id}/documents`),
    {
      method: "POST",
      body: formData,
    }
  );
  if (!response.ok) {
    // Try to get detailed error message from response body
    try {
      const errorData = await response.json();
      const errorMessage = errorData.detail || response.statusText;
      throw new Error(`${response.status}: ${errorMessage}`);
    } catch (parseError) {
      // If can't parse JSON, use generic message
      throw new Error(`Failed to upload document: ${response.statusText}`);
    }
  }
  return response.json();
}

export async function deleteDocument(
  knowledgeBaseId: string,
  documentId: string
): Promise<void> {
  const response = await fetch(
    resolveServiceURL(`knowledge-bases/${knowledgeBaseId}/documents/${documentId}`),
    {
      method: "DELETE",
    }
  );
  if (!response.ok) {
    throw new Error(`Failed to delete document: ${response.statusText}`);
  }
}

export async function getDocumentStatus(
  knowledgeBaseId: string,
  documentId: string
): Promise<Document> {
  const response = await fetch(
    resolveServiceURL(`knowledge-bases/${knowledgeBaseId}/documents/${documentId}`)
  );
  if (!response.ok) {
    throw new Error(`Failed to get document status: ${response.statusText}`);
  }
  return response.json();
}

// Search knowledge bases for mention
export async function searchKnowledgeBases(query: string): Promise<KnowledgeBase[]> {
  const response = await fetch(
    resolveServiceURL(`knowledge-bases/search?query=${encodeURIComponent(query)}`)
  );
  if (!response.ok) {
    throw new Error(`Failed to search knowledge bases: ${response.statusText}`);
  }
  return response.json();
} 