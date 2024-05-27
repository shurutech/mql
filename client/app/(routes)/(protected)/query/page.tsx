"use client";

import ChatInterface from "@/app/components/chatInterface";
import { useParams } from "next/navigation";
import React, { use, useEffect } from "react";
import { useSearchParams } from 'next/navigation'

const Query = () => {
  const params = useSearchParams();
  const dbId = params.get('db_id')?.toString()!;
  const executable = params.get('executable') === 'true'; 
  return (
    <div>
      <ChatInterface dbId={dbId} executable={executable}/>
    </div>
  );
};

export default Query;
