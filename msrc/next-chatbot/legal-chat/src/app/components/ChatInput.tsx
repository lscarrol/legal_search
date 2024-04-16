"use client"
import { cn } from "@/lib/utils";

import { FC, HTMLAttributes, useState } from "react";
import ReactTextareaAutosize from "react-textarea-autosize";
import { useMutation, useIsMutating } from "@tanstack/react-query";
import { nanoid } from "nanoid";
import { Message } from "@/lib/validators/message";


interface ChatInputProps extends HTMLAttributes<HTMLDivElement> {}


const ChatInput: FC<ChatInputProps> = ({className, ...props}) => {
    const [input, setInput] = useState<string>('')

    const { mutate: sendMessage, isPending} = useMutation({
        mutationFn: async (message: Message) => {
            // mutation logic
            const response = await fetch('/api/message', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({message: 'hello'})
            })
            return response.body
        },
        onSuccess: () => {
            console.log('message sent')
        }
    })
  return (
    <div {...props} className={cn('border-t border-[#E0D8C0]')}>
      <div className='relative mt-4 flex-1 overflow-hidden rounded-lg border-none outline-none'>
        <ReactTextareaAutosize
          rows={2}
        onKeyDown={(e) => {
            if (e.key === 'Enter' && !e.shiftKey) {
                e.preventDefault()
                const message: Message = {
                    id: nanoid(),
                    isUserMessage: true,
                    text: input
                }
                sendMessage(message)
            }
        }}
          maxRows={4}
          value={input}
          onChange={(e) => setInput(e.target.value)}
          autoFocus
          placeholder='Write a message...'
          className='peer disabled:opacity-50 pr-14 resize-none block w-full border-0 bg-[#FDFBF4] py-1.5 text-gray-900 focus:ring-0 text-sm sm:leading-6'
        />
      </div>
    </div>
  )
}

export default ChatInput;