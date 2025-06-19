// Copyright (c) 2025 Bytedance Ltd. and/or its affiliates
// SPDX-License-Identifier: MIT

import { cn } from "~/lib/utils";

import { Markdown } from "~/components/deer-flow/markdown";

interface Props {
  content: string;
  className?: string;
  isCompleted?: boolean;
}

export function ResearchReportBlock({
  content,
  className,
  isCompleted = false,
}: Props) {
  return (
    <div className={cn("relative", className)}>
      <div className="flex items-center justify-between">
        <h3 className="mb-3 text-lg font-semibold">📄 Final Report</h3>
      </div>
      <Markdown>{content}</Markdown>
    </div>
  );
}
