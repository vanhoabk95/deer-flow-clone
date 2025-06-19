// Copyright (c) 2025 Bytedance Ltd. and/or its affiliates
// SPDX-License-Identifier: MIT

import { useEffect, useState } from "react";

import { env } from "~/env";

import { getConfig } from "./config";

export function useRAGProvider() {
  const [loading, setLoading] = useState(true);
  const [provider, setProvider] = useState<string | null>(null);

  useEffect(() => {
    if (env.NEXT_PUBLIC_STATIC_WEBSITE_ONLY) {
      setLoading(false);
      return;
    }
    // Always use built-in knowledge base provider
    setProvider("knowledge-base");
    setLoading(false);
  }, []);

  return { provider, loading };
}
