"use client";

import ChatInterface from "@/app/components/chatInterface";
import { useParams } from "next/navigation";
import React, { use, useEffect } from "react";
import { useSearchParams } from 'next/navigation'

const Query = () => {
  const params = useSearchParams();
  const dbId = params.get('db_id')?.toString()!;
  return (
    <div>
      <ChatInterface dbId={dbId} />
    </div>
  );
};

export default Query;
