"use client";

import useCodeBlockViewController from "../viewControllers/codeBlockViewController";
import AceEditor from 'react-ace';
import 'ace-builds/src-noconflict/mode-sql';
import 'ace-builds/src-noconflict/theme-monokai';

type Props = {
  handleQueryResponse: () => void;
  codeString: string;
  dbId: string;
  setSql : (sql: string) => void;
};

const CodeBlock = ({ handleQueryResponse , codeString, dbId, setSql }: Props) => {
  
  const {
    handleCopyClick,
    copySuccess,
    executeSuccess,
    query,
    handleQueryChange,
    handleExecuteClick
  } = useCodeBlockViewController({ codeString, dbId, setSql, handleQueryResponse});
  
  return (
    <div className="relative rounded-md overflow-hidden">
      <AceEditor
        mode="sql"
        theme="monokai"
        onChange={handleQueryChange}
        value={query}
        width="100%"
        height='200px'
        setOptions={{
          enableBasicAutocompletion: true,
          enableLiveAutocompletion: true,
          enableSnippets: true,
          showLineNumbers: true,
          tabSize: 1,
          wrap: true,
          fontSize: 14,
          showPrintMargin: false,
        }}
      />

      <div className="absolute bottom-2 right-0 mt-2">
        
      <button
        className=" mr-2 px-3 py-1 text-sm bg-gray-100 text-gray-600 rounded-sm"
        onClick={handleExecuteClick}
      >
        {executeSuccess ? "Executed" : "Execute"}
      </button>
      <button
        className=" mr-2 px-3 py-1 text-sm bg-gray-100 text-gray-600 rounded-sm"
        onClick={handleCopyClick}
      >
        {copySuccess ? "Copied!" : "Copy"}
      </button>
      </div>
    </div>
  );
};

export default CodeBlock;
