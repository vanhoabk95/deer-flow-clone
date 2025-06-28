// Copyright (c) 2025 Bytedance Ltd. and/or its affiliates
// SPDX-License-Identifier: MIT

import { create } from "zustand";

// Define MCP types locally since the mcp module is empty
interface MCPServerMetadata {
  name: string;
  enabled: boolean;
  transport: string;
  env?: Record<string, string>;
  command?: string;
  args?: string[];
  url?: string;
  tools: Array<{ name: string }>;
}

interface SimpleMCPServerMetadata {
  name: string;
  transport: string;
  env?: Record<string, string>;
  command?: string;
  args?: string[];
  url?: string;
}

const SETTINGS_KEY = "deerflow.settings";

const DEFAULT_SETTINGS: SettingsState = {
  general: {
    autoAcceptedPlan: false,


    maxPlanIterations: 1,
    maxStepNum: 3,
    maxSearchResults: 3,
          reportStyle: "issue_history",
  },
  mcp: {
    servers: [],
  },
};

export type SettingsState = {
  general: {
    autoAcceptedPlan: boolean;


    maxPlanIterations: number;
    maxStepNum: number;
    maxSearchResults: number;
    reportStyle: "issue_history" | "risk_assessment" | "working_guide" | "common_knowledge";
  };
  mcp: {
    servers: MCPServerMetadata[];
  };
};

export const useSettingsStore = create<SettingsState>(() => ({
  ...DEFAULT_SETTINGS,
}));

export const useSettings = (key: keyof SettingsState) => {
  return useSettingsStore((state) => state[key]);
};

export const changeSettings = (settings: SettingsState) => {
  useSettingsStore.setState(settings);
};

export const loadSettings = () => {
  if (typeof window === "undefined") {
    return;
  }
  const json = localStorage.getItem(SETTINGS_KEY);
  if (json) {
    const settings = JSON.parse(json);
    for (const key in DEFAULT_SETTINGS.general) {
      if (!(key in settings.general)) {
        settings.general[key as keyof SettingsState["general"]] =
          DEFAULT_SETTINGS.general[key as keyof SettingsState["general"]];
      }
    }

    try {
      useSettingsStore.setState(settings);
    } catch (error) {
      console.error(error);
    }
  }
};

export const saveSettings = () => {
  const latestSettings = useSettingsStore.getState();
  const json = JSON.stringify(latestSettings);
  localStorage.setItem(SETTINGS_KEY, json);
};

export const getChatStreamSettings = () => {
  let mcpSettings:
    | {
        servers: Record<
          string,
          MCPServerMetadata & {
            enabled_tools: string[];
            add_to_agents: string[];
          }
        >;
      }
    | undefined = undefined;
  const { mcp, general } = useSettingsStore.getState();
  const mcpServers = mcp.servers.filter((server) => server.enabled);
  if (mcpServers.length > 0) {
    mcpSettings = {
      servers: mcpServers.reduce((acc, cur) => {
        const { transport, env } = cur;
        let server: SimpleMCPServerMetadata;
        if (transport === "stdio") {
          server = {
            name: cur.name,
            transport,
            env,
            command: cur.command,
            args: cur.args,
          };
        } else {
          server = {
            name: cur.name,
            transport,
            env,
            url: cur.url,
          };
        }
        return {
          ...acc,
          [cur.name]: {
            ...server,
            enabled_tools: cur.tools.map((tool) => tool.name),
            add_to_agents: ["researcher"],
          },
        };
      }, {}),
    };
  }
  return {
    ...general,
    mcpSettings,
  };
};

export function setReportStyle(
      value: "issue_history" | "risk_assessment" | "working_guide" | "common_knowledge",
) {
  useSettingsStore.setState((state) => ({
    general: {
      ...state.general,
      reportStyle: value,
    },
  }));
  saveSettings();
}




loadSettings();
