// Copyright (c) 2025 Bytedance Ltd. and/or its affiliates
// SPDX-License-Identifier: MIT

import { env } from "~/env";
import type { Resource } from "../messages";
import { fetchStream } from "../sse";

import { resolveServiceURL } from "./resolve-service-url";
import type { ChatEvent } from "./types";

export async function* chatStream(
  userMessage: string,
  params: {
    thread_id: string;
    resources?: Array<Resource>;
    auto_accepted_plan: boolean;
    max_plan_iterations: number;
    max_step_num: number;
    max_search_results?: number;
    interrupt_feedback?: string;
    report_style?: "issue_history" | "risk_assessment" | "working_guide" | "common_knowledge";
  },
  options: { abortSignal?: AbortSignal } = {},
) {
  try{
    // Extract knowledge base IDs from resources
    const knowledge_base = params.resources?.filter(resource => 
      resource.uri?.startsWith('kb://')
    ).map(resource => resource.uri.replace('kb://', '')) || [];
    
    const stream = fetchStream(resolveServiceURL("chat/stream"), {
      body: JSON.stringify({
        messages: [{ role: "user", content: userMessage }],
        ...params,
        knowledge_base,
      }),
      signal: options.abortSignal,
    });
    
    for await (const event of stream) {
      yield {
        type: event.event,
        data: JSON.parse(event.data),
      } as ChatEvent;
    }
  }catch(e){
    console.error(e);
  }
}
