"use client"

import { Card } from "@/components/ui/card"
import { FilePreviewControls } from "./file-preview-controls"
import { useState, useEffect, useRef } from "react"
import { ChevronDown, FileText, ChevronLeft, ChevronRight, Upload } from "lucide-react"
import { Button } from "@/components/ui/button"
import { ScrollArea } from "@/components/ui/scroll-area"
import {
  Collapsible,
  CollapsibleContent,
  CollapsibleTrigger,
} from "@/components/ui/collapsible"
import '@/styles/scrollbar.css'

interface FileItem {
  name: string
  path: string
}

const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:6000'

export function FileSidebar() {
  const [selectedFile, setSelectedFile] = useState<string>('/CAMEL旅游规划助手.pdf')
  const [isOpen, setIsOpen] = useState(true)
  const [isCollapsed, setIsCollapsed] = useState(false)
  const [files, setFiles] = useState<FileItem[]>([])
  const fileInputRef = useRef<HTMLInputElement>(null)

  // 获取 public 目录下的所有 PDF 文件
  const fetchPDFFiles = async () => {
    try {
      const response = await fetch(`${API_URL}/api/files`)
      const data = await response.json()
      const pdfFiles = data.files
        .filter((file: string) => file.endsWith('.pdf'))
        .map((file: string) => ({
          name: file.replace('.pdf', ''),
          path: `/${file}`
        }))
      setFiles(pdfFiles)
    } catch (error) {
      console.error('Error fetching PDF files:', error)
    }
  }

  useEffect(() => {
    fetchPDFFiles()
  }, [])

  const handleDownload = () => {
    const previewElement = document.getElementById('file-preview') as HTMLIFrameElement
    if (previewElement && previewElement.src) {
      const link = document.createElement('a')
      link.href = previewElement.src
      const fileName = previewElement.src.split('/').pop() || 'downloaded-file'
      link.download = fileName
      document.body.appendChild(link)
      link.click()
      document.body.removeChild(link)
    }
  }

  const handleUploadClick = () => {
    fileInputRef.current?.click()
  }

  const handleFileUpload = async (event: React.ChangeEvent<HTMLInputElement>) => {
    const file = event.target.files?.[0]
    if (!file) return

    if (!file.type.includes('pdf')) {
      alert('只能上传 PDF 文件!')
      return
    }

    const formData = new FormData()
    formData.append('file', file)

    try {
      const response = await fetch(`${API_URL}/api/upload`, {
        method: 'POST',
        body: formData
      })

      if (response.ok) {
        // 重新获取文件列表
        fetchPDFFiles()
      } else {
        alert('上传失败，请重试')
      }
    } catch (error) {
      console.error('Error uploading file:', error)
      alert('上传失败，请重试')
    }

    // 清空 input 的值，这样相同的文件可以再次上传
    if (fileInputRef.current) {
      fileInputRef.current.value = ''
    }
  }

  return (
    <div className={`relative flex flex-col border-l border-gray-200 dark:border-gray-700 bg-white dark:bg-gray-800 transition-all duration-300 ${isCollapsed ? 'w-16' : 'w-[400px]'}`}>
      <Button 
        variant="ghost" 
        size="sm" 
        className="absolute -left-4 top-4 z-50 h-8 w-8 rounded-full bg-gray-100 dark:bg-gray-700 p-0"
        onClick={() => setIsCollapsed(!isCollapsed)}
      >
        {isCollapsed ? <ChevronLeft className="h-4 w-4" /> : <ChevronRight className="h-4 w-4" />}
      </Button>

      {!isCollapsed && (
        <>
          <div className="p-4 border-b border-gray-200 dark:border-gray-700">
            <h2 className="text-lg font-semibold text-gray-900 dark:text-gray-100">Files</h2>
          </div>
          <div className="flex flex-col">
            <div className="p-4">
              <Collapsible open={isOpen} onOpenChange={setIsOpen}>
                <div className="flex items-center justify-between mb-2">
                  <CollapsibleTrigger className="flex items-center gap-2 p-2 text-sm font-medium text-gray-900 dark:text-gray-100 text-left hover:bg-gray-100 dark:hover:bg-gray-700 rounded-lg transition-colors">
                    <span>Available Files</span>
                    <ChevronDown className={`h-4 w-4 transition-transform ${isOpen ? 'transform rotate-180' : ''}`} />
                  </CollapsibleTrigger>
                  <Button
                    variant="outline"
                    size="sm"
                    className="text-gray-900 dark:text-gray-100 border-gray-200 dark:border-gray-700 hover:bg-gray-100 dark:hover:bg-gray-700"
                    onClick={handleUploadClick}
                  >
                    <Upload className="h-4 w-4 mr-1" />
                    上传
                  </Button>
                  <input
                    type="file"
                    ref={fileInputRef}
                    accept=".pdf"
                    className="hidden"
                    onChange={handleFileUpload}
                  />
                </div>
                <CollapsibleContent className="mt-1">
                  <ScrollArea className="h-[300px] w-full rounded-md border border-gray-200 dark:border-gray-700">
                    <div className="p-4 space-y-2 custom-scrollbar overflow-y-auto">
                      {files.map((file) => (
                        <button
                          key={file.path}
                          className={`flex items-center gap-2 w-full p-2 text-sm rounded-lg transition-colors text-gray-900 dark:text-gray-100 ${
                            selectedFile === file.path 
                              ? 'bg-gray-200 dark:bg-gray-600' 
                              : 'hover:bg-gray-100 dark:hover:bg-gray-700'
                          }`}
                          onClick={() => setSelectedFile(file.path)}
                        >
                          <FileText className="h-4 w-4 flex-shrink-0 text-gray-600 dark:text-gray-400" />
                          <span className="truncate">{file.name}</span>
                        </button>
                      ))}
                    </div>
                  </ScrollArea>
                </CollapsibleContent>
              </Collapsible>
            </div>
            
            <Card className="mx-4 mb-4 bg-white dark:bg-gray-800 border-gray-200 dark:border-gray-700">
              <div className="text-sm font-medium p-4 border-b border-gray-200 dark:border-gray-700 text-gray-900 dark:text-gray-100">
                Preview
              </div>
              <div className="relative">
                <iframe
                  id="file-preview"
                  className="w-full h-[calc(100vh-280px)] bg-white dark:bg-gray-800"
                  src={selectedFile}
                  style={{ border: 'none' }}
                />
                <FilePreviewControls 
                  onDownload={handleDownload} 
                  currentFile={selectedFile.split('/').pop() || ''}
                />
              </div>
            </Card>
          </div>
        </>
      )}
      
      {isCollapsed && (
        <div className="flex flex-col items-center py-4">
          <FileText className="h-6 w-6 text-gray-500" />
        </div>
      )}
    </div>
  )
}

