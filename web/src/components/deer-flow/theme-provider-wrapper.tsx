// Copyright (c) 2025 Bytedance Ltd. and/or its affiliates
// SPDX-License-Identifier: MIT

"use client";

import { usePathname } from "next/navigation";

import { ThemeProvider } from "~/components/theme-provider";

export function ThemeProviderWrapper({
  children,
}: {
  children: React.ReactNode;
}) {
  const pathname = usePathname();
  const isChatPage = pathname?.startsWith("/chat");
  const isKnowledgeBasePage = pathname?.startsWith("/knowledge-base");
  const isThemeToggleEnabledPage = isChatPage || isKnowledgeBasePage;

  return (
    <ThemeProvider
      attribute="class"
      defaultTheme={"dark"}
      enableSystem={isThemeToggleEnabledPage}
      forcedTheme={isThemeToggleEnabledPage ? undefined : "dark"}
      disableTransitionOnChange
    >
      {children}
    </ThemeProvider>
  );
}
