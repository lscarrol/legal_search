"use client"
import { AccordionContent, AccordionTrigger } from "@/components/ui/accordion";
import ChatHeader from "./ChatHeader";
import ChatInput from "./ChatInput";
import { Accordion, AccordionItem } from "@radix-ui/react-accordion";
import { FC } from "react";

const Chat: FC = () => {
  return (
    <Accordion type='single' collapsible className="relative z-40">
      <AccordionItem value='item-1'>
        <div className="fixed bottom-8 left-1/2 transform -translate-x-1/2 w-[1000px] bg-[#FDFBF4] border border-[#E0D8C0] rounded-md overflow-hidden shadow-lg">
          <div className="w-full h-full flex flex-col">
            <AccordionTrigger className='px-6 border-b border-[#E0D8C0]'>
              <ChatHeader />
            </AccordionTrigger>
            <AccordionContent>
              <div className='flex flex-col h-80'>
                messages
                <ChatInput className='px-4'/>
              </div>
            </AccordionContent>
          </div>
        </div>
      </AccordionItem>
    </Accordion>
  )
}

export default Chat;