"use client";

import ChatInterface from "@/app/components/chatInterface";
import React from "react";
import { useSearchParams } from 'next/navigation'

const Query:React.FC = () => {
  const params = useSearchParams();
  const dbId = params.get('db_id')?.toString()!;
  return (
    <div>
      <ChatInterface dbId={dbId}/>
    </div>
  );
};

export default Query;
