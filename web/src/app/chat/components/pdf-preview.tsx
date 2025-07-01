// Copyright (c) 2025 Bytedance Ltd. and/or its affiliates
// SPDX-License-Identifier: MIT

import React, { useState } from "react";
import { FileText, ExternalLink } from "lucide-react";
import { Button } from "~/components/ui/button";
import { Card } from "~/components/ui/card";
import { 
  Select, 
  SelectContent, 
  SelectItem, 
  SelectTrigger, 
  SelectValue 
} from "~/components/ui/select";
import { resolveServiceURL } from "~/core/api/resolve-service-url";

type AspectRatio = "1/1.41" | "4/3" | "16/9" | "3/4" | "1/1" | "3/2";

interface PDFPreviewProps {
  fileName: string;
  knowledgeBase: string;
  pages: number[];
  className?: string;
  height?: number;
  aspectRatio?: AspectRatio;
}

const aspectRatioOptions = [
  { value: "4/3" as AspectRatio, label: "4:3 (Default)" },
  { value: "1/1.41" as AspectRatio, label: "1:1.41 (A4)" },
  { value: "16/9" as AspectRatio, label: "16:9 (Wide)" },
  { value: "3/4" as AspectRatio, label: "3:4 (Portrait)" },
  { value: "1/1" as AspectRatio, label: "1:1 (Square)" },
  { value: "3/2" as AspectRatio, label: "3:2 (Image)" },
];

// Hàm helper để convert aspect ratio string sang CSS value
const getAspectRatioValue = (ratio: AspectRatio): string => {
  switch (ratio) {
    case "1/1.41": return "1 / 1.41";
    case "4/3": return "4 / 3";
    case "16/9": return "16 / 9";
    case "3/4": return "3 / 4";
    case "1/1": return "1 / 1";
    case "3/2": return "3 / 2";
    default: return "4 / 3";
  }
};

export function PDFPreview({ 
  fileName, 
  knowledgeBase, 
  pages, 
  className, 
  height = 400,
  aspectRatio: initialAspectRatio = "4/3"
}: PDFPreviewProps) {
  const [selectedAspectRatio, setSelectedAspectRatio] = useState<AspectRatio>(initialAspectRatio);
  const pdfUrl = resolveServiceURL(`knowledge-bases/${knowledgeBase}/documents/${fileName}/pdf`);

  const handleOpenPDF = () => {
    window.open(pdfUrl, '_blank');
  };

  const handleAspectRatioChange = (value: string) => {
    setSelectedAspectRatio(value as AspectRatio);
  };

  if (!pages || pages.length === 0) {
    return null;
  }

  return (
    <Card className={`w-full max-w-full ${className || ''}`} style={{ boxShadow: 'none', border: 'none', background: 'transparent' }}>
      <div className="flex items-center gap-2 mb-2">
        <FileText size={18} className="text-red-500" />
        <span className="font-medium text-base truncate">{fileName}</span>
        <div className="ml-auto flex items-center gap-2">
          <Select value={selectedAspectRatio} onValueChange={handleAspectRatioChange}>
            <SelectTrigger className="w-[140px] h-8 text-xs">
              <SelectValue placeholder="Tỷ lệ" />
            </SelectTrigger>
            <SelectContent>
              {aspectRatioOptions.map((option) => (
                <SelectItem key={option.value} value={option.value} className="text-xs">
                  {option.label}
                </SelectItem>
              ))}
            </SelectContent>
          </Select>
          <Button
            variant="outline"
            size="sm"
            className="flex-shrink-0"
            onClick={handleOpenPDF}
          >
            <ExternalLink size={14} className="mr-1" />
            Open Full PDF
          </Button>
        </div>
      </div>
      {/* Render từng trang PDF liên quan */}
      {pages.map((page) => (
        <div key={page} className="mb-6 w-full max-w-full">
          <div className="text-xs text-muted-foreground mb-1">Page {page}</div>
          <div 
            className="w-full max-w-full overflow-hidden border rounded-md"
            style={{ 
              aspectRatio: getAspectRatioValue(selectedAspectRatio)
            }}
          >
            <iframe
              src={`${pdfUrl}#page=${page}&toolbar=0&navpanes=0&scrollbar=0&view=Fit&zoom=page-fit&pagemode=none&statusbar=0&messages=0&printtool=0`}
              className="w-full h-full border-0 pointer-events-none"
              title={`PDF Preview - ${fileName} - Page ${page}`}
              style={{ 
                overflow: 'hidden',
                margin: 0,
                padding: 0
              }}
            />
          </div>
        </div>
      ))}
    </Card>
  );
} 