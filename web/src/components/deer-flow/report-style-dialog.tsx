// Copyright (c) 2025 Bytedance Ltd. and/or its affiliates
// SPDX-License-Identifier: MIT

import { useState } from "react";
import { Check, FileText, Newspaper, Users, GraduationCap, FileSearch, ClipboardPenLine, FlaskConical, ContactRound } from "lucide-react";

import { Button } from "~/components/ui/button";
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "~/components/ui/dialog";
import { setReportStyle, useSettingsStore } from "~/core/store";
import { cn } from "~/lib/utils";

import { Tooltip } from "./tooltip";

const REPORT_STYLES = [
  {
    value: "academic" as const,
    label: "Academic",
    description: "Formal, objective, and analytical with precise terminology",
    icon: GraduationCap,
  },
  {
    value: "popular_science" as const,
    label: "Popular Science",
    description: "Engaging and accessible for general audience",
    icon: FileText,
  },
  {
    value: "news" as const,
    label: "News",
    description: "Factual, concise, and impartial journalistic style",
    icon: Newspaper,
  },
  {
    value: "social_media" as const,
    label: "Social Media",
    description: "Concise, attention-grabbing, and shareable",
    icon: Users,
  },
  {
    value: "issue_history" as const,
    label: "Issue History",
    description: "Suggest analyze base on issue history",
    icon: FileSearch,
  },
  {
    value: "risk_assessment" as const,
    label: "Risk Assessment",
    description: "Suggest check items, potential risks",
    icon: FlaskConical,
  },
  {
    value: "working_guide" as const,
    label: "Working Guide",
    description: "Guide step by step to do a work",
    icon: ClipboardPenLine,
  },
  {
    value: "common_knowledge" as const,
    label: "Common Knowledge",
    description: "Q&A about common knowledge, policies, training, rules",
    icon: ContactRound,
  },
];

export function ReportStyleDialog() {
  const [open, setOpen] = useState(false);
  const currentStyle = useSettingsStore((state) => state.general.reportStyle);

  const handleStyleChange = (
    style: "academic" | "popular_science" | "news" | "social_media",
  ) => {
    setReportStyle(style);
    setOpen(false);
  };

  const currentStyleConfig =
    REPORT_STYLES.find((style) => style.value === currentStyle) ||
    REPORT_STYLES[0]!;
  const CurrentIcon = currentStyleConfig.icon;

  return (
    <Dialog open={open} onOpenChange={setOpen}>
      <Tooltip
        className="max-w-60"
        title={
          <div>
            <h3 className="mb-2 font-bold">
              Writing Style: {currentStyleConfig.label}
            </h3>
            <p>
              Choose the writing style for your research reports. Different
              styles are optimized for different audiences and purposes.
            </p>
          </div>
        }
      >
        <DialogTrigger asChild>
          <Button
            className="!border-brand !text-brand rounded-2xl"
            variant="outline"
          >
            <CurrentIcon className="h-4 w-4" /> {currentStyleConfig.label}
          </Button>
        </DialogTrigger>
      </Tooltip>
      <DialogContent className="sm:max-w-[500px]">
        <DialogHeader>
          <DialogTitle>Choose Research Category</DialogTitle>
          <DialogDescription>
            Select the research category for your research. Each category is
            optimized for different purposes.
          </DialogDescription>
        </DialogHeader>
        <div className="grid gap-3 py-4">
          {REPORT_STYLES.map((style) => {
            const Icon = style.icon;
            const isSelected = currentStyle === style.value;

            return (
              <button
                key={style.value}
                className={cn(
                  "hover:bg-accent flex items-start gap-3 rounded-lg border p-4 text-left transition-colors",
                  isSelected && "border-primary bg-accent",
                )}
                onClick={() => handleStyleChange(style.value)}
              >
                <Icon className="mt-0.5 h-5 w-5 shrink-0" />
                <div className="flex-1 space-y-1">
                  <div className="flex items-center gap-2">
                    <h4 className="font-medium">{style.label}</h4>
                    {isSelected && <Check className="text-primary h-4 w-4" />}
                  </div>
                  <p className="text-muted-foreground text-sm">
                    {style.description}
                  </p>
                </div>
              </button>
            );
          })}
        </div>
      </DialogContent>
    </Dialog>
  );
}
