// Copyright (c) 2025 Bytedance Ltd. and/or its affiliates
// SPDX-License-Identifier: MIT

"use client";

import { MessageSquare } from "lucide-react";
import { Button } from "~/components/ui/button";
import { Logo } from "~/components/deer-flow/logo";
import { ThemeToggle } from "~/components/deer-flow/theme-toggle";
import { SettingsDialog } from "~/app/settings/dialogs/settings-dialog";
import Link from "next/link";
import { Suspense } from "react";

export function PageHeader() {
  return (
    <header className="flex h-12 w-full items-center justify-between px-3 sm:px-4 z-50 bg-background/80 backdrop-blur-sm border-b flex-shrink-0">
      <Logo />
      <div className="flex items-center space-x-2">
        <Link href="/chat">
          <Button variant="ghost" size="sm" className="text-xs sm:text-sm">
            <MessageSquare className="w-4 h-4 mr-1 sm:mr-2" />
            <span className="hidden sm:inline">Chat</span>
          </Button>
        </Link>
        <ThemeToggle />
        <Suspense>
          <SettingsDialog />
        </Suspense>
      </div>
    </header>
  );
} 