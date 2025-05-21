"use client"

import { useState } from "react"
import { Button } from "@/components/ui/button"
import {
  Dialog,
  DialogContent,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "@/components/ui/dialog"
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select"
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"

interface SettingsModalProps {
  open: boolean
  onOpenChange: (open: boolean) => void
}

export function SettingsModal({ open, onOpenChange }: SettingsModalProps) {
  const [modelType, setModelType] = useState("")
  const [apiKey, setApiKey] = useState("")
  const [baseUrl, setBaseUrl] = useState("")

  const handleSave = () => {
    // Here you would typically save these settings to your state management solution or backend
    console.log("Settings saved:", { modelType, apiKey, baseUrl })
    onOpenChange(false)
  }

  return (
    <Dialog open={open} onOpenChange={onOpenChange}>
      <DialogContent className="sm:max-w-[425px]">
        <DialogHeader>
          <DialogTitle className="text-gray-900 dark:text-gray-100">Settings</DialogTitle>
        </DialogHeader>
        <div className="grid gap-4 py-4">
          <div className="grid grid-cols-4 items-center gap-4">
            <Label htmlFor="model-type" className="text-right text-gray-700 dark:text-gray-300">
              Model Type
            </Label>
            <Select value={modelType} onValueChange={setModelType}>
              <SelectTrigger className="col-span-3 bg-white dark:bg-gray-800 border-gray-200 dark:border-gray-700">
                <SelectValue placeholder="Select model type" className="text-gray-900 dark:text-gray-100" />
              </SelectTrigger>
              <SelectContent className="bg-white dark:bg-gray-800 border-gray-200 dark:border-gray-700">
                <SelectItem value="Qwen2.5-72B-Instruct" className="text-gray-900 dark:text-gray-100">Qwen2.5-72B-Instruct</SelectItem>
                <SelectItem value="gpt-4o" className="text-gray-900 dark:text-gray-100">gpt-4o</SelectItem>
                <SelectItem value="gpt-4.5-preview" className="text-gray-900 dark:text-gray-100">gpt-4.5-preview</SelectItem>
                <SelectItem value="claude-3.5-sonnet" className="text-gray-900 dark:text-gray-100">claude-3.5-sonnet</SelectItem>
                <SelectItem value="claude-3.7-sonnet" className="text-gray-900 dark:text-gray-100">claude-3.7-sonnet</SelectItem>
                <SelectItem value="o1" className="text-gray-900 dark:text-gray-100">o1</SelectItem>
                <SelectItem value="o3-mini" className="text-gray-900 dark:text-gray-100">o3-mini</SelectItem>
              </SelectContent>
            </Select>
          </div>
          <div className="grid grid-cols-4 items-center gap-4">
            <Label htmlFor="api-key" className="text-right text-gray-700 dark:text-gray-300">
              API Key
            </Label>
            <Input
              id="api-key"
              value={apiKey}
              onChange={(e) => setApiKey(e.target.value)}
              className="col-span-3 bg-white dark:bg-gray-800 border-gray-200 dark:border-gray-700 text-gray-900 dark:text-gray-100"
            />
          </div>
          <div className="grid grid-cols-4 items-center gap-4">
            <Label htmlFor="base-url" className="text-right text-gray-700 dark:text-gray-300">
              Base URL
            </Label>
            <Input
              id="base-url"
              value={baseUrl}
              onChange={(e) => setBaseUrl(e.target.value)}
              className="col-span-3 bg-white dark:bg-gray-800 border-gray-200 dark:border-gray-700 text-gray-900 dark:text-gray-100"
            />
          </div>
        </div>
        <Button onClick={handleSave} className="bg-gray-900 dark:bg-gray-700 hover:bg-gray-800 dark:hover:bg-gray-600 text-white">Save Changes</Button>
      </DialogContent>
    </Dialog>
  )
}

