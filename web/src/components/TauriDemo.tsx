'use client'

import { useState, useEffect } from 'react'
import { isTauri, useTauriWindow, getPlatform } from '~/lib/tauri'
import { Button } from '~/components/ui/button'
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '~/components/ui/card'

export function TauriDemo() {
  const [platform, setPlatform] = useState<string | null>(null)
  const [windowTitle, setWindowTitle] = useState('')
  const window = useTauriWindow()

  useEffect(() => {
    if (isTauri()) {
      setPlatform(getPlatform())
    }
  }, [])

  const handleMinimize = async () => {
    try {
      await window?.minimize()
    } catch (error) {
      console.error('Error minimizing window:', error)
    }
  }

  const handleMaximize = async () => {
    try {
      await window?.maximize()
    } catch (error) {
      console.error('Error maximizing window:', error)
    }
  }

  const handleSetTitle = async () => {
    try {
      await window?.setTitle(windowTitle || 'Deer Flow')
    } catch (error) {
      console.error('Error setting window title:', error)
    }
  }

  if (!isTauri()) {
    return (
      <Card className="w-full max-w-md mx-auto">
        <CardHeader>
          <CardTitle>🌐 Web Version</CardTitle>
          <CardDescription>
            Bạn đang sử dụng phiên bản web. Để trải nghiệm các tính năng desktop, 
            hãy chạy ứng dụng với Tauri.
          </CardDescription>
        </CardHeader>
      </Card>
    )
  }

  return (
    <Card className="w-full max-w-md mx-auto">
      <CardHeader>
        <CardTitle>🖥️ Desktop Version</CardTitle>
        <CardDescription>
          Ứng dụng đang chạy trong Tauri trên {platform || 'unknown'}
        </CardDescription>
      </CardHeader>
      <CardContent className="space-y-4">
        <div className="space-y-2">
          <label htmlFor="window-title" className="text-sm font-medium">
            Tiêu đề cửa sổ:
          </label>
          <input
            id="window-title"
            type="text"
            value={windowTitle}
            onChange={(e) => setWindowTitle(e.target.value)}
            placeholder="Nhập tiêu đề mới..."
            className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
          />
          <Button onClick={handleSetTitle} className="w-full">
            Đổi tiêu đề
          </Button>
        </div>

        <div className="flex space-x-2">
          <Button onClick={handleMinimize} variant="outline" className="flex-1">
            Thu nhỏ
          </Button>
          <Button onClick={handleMaximize} variant="outline" className="flex-1">
            Phóng to
          </Button>
        </div>

        <div className="text-sm text-gray-600">
          <p><strong>Platform:</strong> {platform}</p>
          <p><strong>Tauri:</strong> ✅ Đã kích hoạt</p>
        </div>
      </CardContent>
    </Card>
  )
} 