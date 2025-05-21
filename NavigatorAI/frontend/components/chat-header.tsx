interface ChatHeaderProps {
  title: string
  currentStage?: string
}

export function ChatHeader({ title }: ChatHeaderProps) {
  return (
    <div className="flex-1 flex items-center justify-between px-4 py-3 border-b dark:border-gray-800">
      <div className="flex items-center gap-2">
        <div className="flex flex-col">
          <span className="text-lg font-medium text-gray-800 dark:text-gray-200">
            NavigatorAI
          </span>
          <span className="text-sm text-gray-500 dark:text-gray-400">
            注意，该项目仅供<a href="https://github.com/datawhalechina/handy-multi-agent" className="underline" target="_blank" rel="noopener noreferrer">handy-multi-agent</a>参考，请勿用于商业用途，目前由<a href="https://github.com/Tsumugii24" className="underline" target="_blank" rel="noopener noreferrer">Tsumugii24</a>维护
          </span>
        </div>
      </div>
    </div>
  )
}

