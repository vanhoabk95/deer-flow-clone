// Copyright (c) 2025 Bytedance Ltd. and/or its affiliates
// SPDX-License-Identifier: MIT

"use client";

import { useEffect } from "react";
import { useKnowledgeBaseStore } from "~/core/store/knowledge-base-store";
import { 
  CreateKnowledgeBaseDialog, 
  KnowledgeBaseList, 
  PageHeader 
} from "./components";

export default function KnowledgeBasePage() {
  const { fetchKnowledgeBases } = useKnowledgeBaseStore();

  useEffect(() => {
    fetchKnowledgeBases();
  }, [fetchKnowledgeBases]);

  return (
    <div className="flex h-screen w-screen flex-col overscroll-none">
      {/* Header */}
      <PageHeader />

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

          <KnowledgeBaseList onRefresh={fetchKnowledgeBases} />
        </div>
      </div>
    </div>
  );
} 