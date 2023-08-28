'use client';

import React from 'react';
import * as Accordion from '@radix-ui/react-accordion';
import AccordionContent from '@/lib/components/ui/accordion/context';
import AccordionTrigger from '@/lib/components/ui/accordion/trigger';
import AccordionItem from '@/lib/components/ui/accordion/items';

const Leaderboard = () => {
  return (
    <Accordion.Root
      className="w-[50vw] rounded-md shadow-[0_2px_10px] shadow-black/5"
      type="single"
      defaultValue="item-1"
      collapsible
    >
      <AccordionItem value="item-1" className="mb-10">
        <AccordionTrigger>Is it accessible?</AccordionTrigger>
        <AccordionContent>
          Yes. It adheres to the WAI-ARIA design pattern.
        </AccordionContent>
      </AccordionItem>

      <AccordionItem value="item-2" className="mb-10">
        <AccordionTrigger>Is it unstyled?</AccordionTrigger>
        <AccordionContent>
          Yes. It's unstyled by default, giving you freedom over the look and
          feel.
        </AccordionContent>
      </AccordionItem>

      <AccordionItem value="item-3" className="mb-10">
        <AccordionTrigger>Can it be animated?</AccordionTrigger>
        <AccordionContent>
          Yes! You can animate the Accordion with CSS or JavaScript.
        </AccordionContent>
      </AccordionItem>
    </Accordion.Root>
  );
};

export default Leaderboard;
