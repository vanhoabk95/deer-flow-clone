// Copyright (c) 2025 Bytedance Ltd. and/or its affiliates
// SPDX-License-Identifier: MIT

"use client";

import { useKnowledgeBaseStore } from "~/core/store/knowledge-base-store";
import { Card, CardContent, CardHeader } from "~/components/ui/card";
import { Skeleton } from "~/components/ui/skeleton";
import { KnowledgeBaseCard } from "./knowledge-base-card";

interface KnowledgeBaseListProps {
  onRefresh: () => void;
}

export function KnowledgeBaseList({ onRefresh }: KnowledgeBaseListProps) {
  const { knowledgeBases, loading } = useKnowledgeBaseStore();

  if (loading) {
    return (
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
    );
  }

  if (knowledgeBases.length === 0) {
    return (
      <div className="text-center py-8 sm:py-12">
        <p className="text-gray-700 dark:text-gray-300 text-lg sm:text-xl font-semibold">
          Get started by creating your first knowledge base
        </p>
      </div>
    );
  }

  return (
    <div className="grid gap-3 sm:gap-4 lg:gap-6 grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 auto-rows-fr">
      {knowledgeBases.map((knowledgeBase) => (
        <div key={knowledgeBase.id} className="w-full max-w-full">
          <KnowledgeBaseCard
            knowledgeBase={knowledgeBase}
            onRefresh={onRefresh}
          />
        </div>
      ))}
    </div>
  );
} 