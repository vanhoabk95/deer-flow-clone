export interface ModelConfig {
  [provider: string]: string[];
}

export interface DeerFlowConfig {
  models: ModelConfig;
}
