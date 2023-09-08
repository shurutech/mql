"use client";

import { useState } from "react";
import { Prism as SyntaxHighlighter } from "react-syntax-highlighter";
import { kimbieDark } from "react-syntax-highlighter/dist/esm/styles/hljs";

type Props = {
  codeString: string;
  language: string;
};

const CodeBlock = ({ codeString, language }: Props) => {
  const [copySuccess, setCopySuccess] = useState(false);

  const handleCopyClick = () => {
    navigator.clipboard.writeText(codeString);
    setCopySuccess(true);
    setTimeout(() => setCopySuccess(false), 1500);
  };

  return (
    <div className="relative rounded-md overflow-hidden">
      <SyntaxHighlighter language={language} style={kimbieDark}>
        {codeString}
      </SyntaxHighlighter>
      <button
        className="absolute top-0 right-0 mt-2 mr-2 px-3 py-1 text-sm bg-gray-100 text-gray-600 rounded-sm"
        onClick={handleCopyClick}
      >
        {copySuccess ? "Copied!" : "Copy"}
      </button>
    </div>
  );
};

export default CodeBlock;
