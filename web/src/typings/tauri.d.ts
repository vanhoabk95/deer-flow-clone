/**
 * Tauri type definitions
 */

declare global {
  interface Window {
    __TAURI__?: {
      core?: {
        platform?: string
      }
      [key: string]: unknown
    }
    webpackChunk_N_E?: unknown[]
  }
}

export {} 