// Copyright (c) 2025 Bytedance Ltd. and/or its affiliates
// SPDX-License-Identifier: MIT

"use client";

import dynamic from "next/dynamic";
import { Suspense } from "react";

import { Logo } from "../../components/deer-flow/logo";
import { ThemeToggle } from "../../components/deer-flow/theme-toggle";
import { SettingsDialog } from "../settings/dialogs/settings-dialog";
import { Button } from "../../components/ui/button";
import { Database } from "lucide-react";
import Link from "next/link";

const Main = dynamic(() => import("./main"), {
  ssr: false,
  loading: () => (
    <div className="flex h-full w-full items-center justify-center">
      Loading DeerFlow...
    </div>
  ),
});

export default function HomePage() {
  return (
    <div className="flex h-screen w-screen justify-center overscroll-none">
      <header className="fixed top-0 left-0 flex h-12 w-full items-center justify-between px-4 z-50 bg-background/80 backdrop-blur-sm border-b">
        <Logo />
        <div className="flex items-center space-x-2">
          <Link href="/knowledge-base">
            <Button variant="ghost" size="sm">
              <Database className="w-4 h-4 mr-2" />
              Knowledge Base
            </Button>
          </Link>
          <ThemeToggle />
          <Suspense>
            <SettingsDialog />
          </Suspense>
        </div>
      </header>
      <Main />
    </div>
  );
}
