// Copyright (c) 2025 Bytedance Ltd. and/or its affiliates
// SPDX-License-Identifier: MIT

import React from "react";
import { FileText, ExternalLink } from "lucide-react";
import { Button } from "~/components/ui/button";
import { Card } from "~/components/ui/card";
import { resolveServiceURL } from "~/core/api/resolve-service-url";

interface PDFPreviewProps {
  fileName: string;
  knowledgeBase: string;
  pages: number[];
  className?: string;
  height?: number;
}

export function PDFPreview({ fileName, knowledgeBase, pages, className, height = 400 }: PDFPreviewProps) {
  const pdfUrl = resolveServiceURL(`knowledge-bases/${knowledgeBase}/documents/${fileName}/pdf`);

  const handleOpenPDF = () => {
    window.open(pdfUrl, '_blank');
  };

  if (!pages || pages.length === 0) {
    return null;
  }

  return (
    <Card className={`w-full max-w-full ${className || ''}`} style={{ boxShadow: 'none', border: 'none', background: 'transparent' }}>
      <div className="flex items-center gap-2 mb-2">
        <FileText size={18} className="text-red-500" />
        <span className="font-medium text-base truncate">{fileName}</span>
        <Button
          variant="outline"
          size="sm"
          className="ml-auto flex-shrink-0"
          onClick={handleOpenPDF}
        >
          <ExternalLink size={14} className="mr-1" />
          Open Full PDF
        </Button>
      </div>
      {/* Render từng trang PDF liên quan */}
      {pages.map((page) => (
        <div key={page} className="mb-6 w-full max-w-full">
          <div className="text-xs text-muted-foreground mb-1">Page {page}</div>
          <div className="w-full max-w-full min-w-[300px] aspect-[4/5] min-h-[200px] max-h-[600px]">
            <iframe
              src={`${pdfUrl}#page=${page}&toolbar=0&navpanes=0&scrollbar=0&view=FitH`}
              className="w-full h-full border-0 rounded"
              title={`PDF Preview - ${fileName} - Page ${page}`}
            />
          </div>
        </div>
      ))}
    </Card>
  );
} 