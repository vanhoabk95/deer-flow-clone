// Copyright (c) 2025 Bytedance Ltd. and/or its affiliates
// SPDX-License-Identifier: MIT

import { Edit3, RotateCcw } from "lucide-react";
import { useCallback, useState } from "react";

import { Button } from "~/components/ui/button";
import { cn } from "~/lib/utils";

import { Markdown } from "~/components/deer-flow/markdown";

interface Props {
  content: string;
  className?: string;
  onEdit?: (content: string) => void;
  isCompleted?: boolean;
}

export function ResearchReportBlock({
  content,
  className,
  onEdit,
  isCompleted = false,
}: Props) {
  const [editing, setEditing] = useState(false);
  const [editingContent, setEditingContent] = useState(content);

  const handleEdit = useCallback(() => {
    setEditing(true);
    setEditingContent(content);
  }, [content]);

  const handleSave = useCallback(() => {
    setEditing(false);
    onEdit?.(editingContent);
  }, [editingContent, onEdit]);

  const handleCancel = useCallback(() => {
    setEditing(false);
    setEditingContent(content);
  }, [content]);

  return (
    <div className={cn("relative", className)}>
      <div className="flex items-center justify-between">
        <h3 className="mb-3 text-lg font-semibold">📄 Final Report</h3>
        {isCompleted && editing ? (
          <div className="flex gap-2">
            <Button size="sm" onClick={handleSave}>
              Save
            </Button>
            <Button variant="outline" size="sm" onClick={handleCancel}>
              <RotateCcw size={16} />
              Cancel
            </Button>
          </div>
        ) : (
          isCompleted && (
            <Button variant="outline" size="sm" onClick={handleEdit}>
              <Edit3 size={16} />
              Edit
            </Button>
          )
        )}
      </div>
      {editing ? (
        <textarea
          className="bg-background border-input ring-ring placeholder:text-muted-foreground min-h-[200px] w-full rounded-md border px-3 py-2 text-sm focus:outline-none focus:ring-2"
          value={editingContent}
          onChange={(e) => setEditingContent(e.target.value)}
          placeholder="Edit your report..."
        />
      ) : (
        <Markdown>{content}</Markdown>
      )}
    </div>
  );
}
