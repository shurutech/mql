"use client";

import ChatInterface from "@/app/components/chatInterface";
import { useParams } from "next/navigation";
import React from "react";

const Query = () => {
  const { id } = useParams();
  return (
    <div>
      <ChatInterface dbId={id} />
    </div>
  );
};

export default Query;
