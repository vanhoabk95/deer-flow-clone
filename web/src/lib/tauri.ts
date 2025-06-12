/**
 * Tauri utility functions và hooks
 */

import { invoke } from '@tauri-apps/api/core'
import { getCurrentWindow } from '@tauri-apps/api/window'

/**
 * Kiểm tra xem ứng dụng có đang chạy trong Tauri không
 */
export const isTauri = (): boolean => {
  return typeof window !== 'undefined' && '__TAURI__' in window
}

/**
 * Hook để sử dụng Tauri window APIs
 */
export const useTauriWindow = () => {
  if (!isTauri()) return null

  return getCurrentWindow()
}

/**
 * Gọi Tauri commands từ frontend
 */
export const invokeCommand = async <T>(command: string, args?: Record<string, unknown>): Promise<T> => {
  if (!isTauri()) {
    throw new Error('Tauri is not available')
  }

  return invoke<T>(command, args)
}

/**
 * Platform detection
 */
export const getPlatform = (): string | null => {
  if (!isTauri()) return null
  
  return window.__TAURI__?.core?.platform ?? null
}

/**
 * Check if running on desktop
 */
export const isDesktop = (): boolean => {
  return isTauri()
} 