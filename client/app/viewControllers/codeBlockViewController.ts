import { useState } from "react";

type Props = {
    codeString: string;
    setSql: (sql: string) => void;
    handleQueryResponse: () => void;
  };

const useCodeBlockViewController = ({ handleQueryResponse, codeString, setSql}: Props) => {
    const [copySuccess, setCopySuccess] = useState(false);
    const [executeSuccess, setExecuteSuccess] = useState(false);
    const [query, setQuery] = useState<string>(codeString);

    const handleQueryChange = (query: string) => {
        setExecuteSuccess(false);
        setQuery(query);
        setSql(query);
    }
    const handleCopyClick = () => {
      navigator.clipboard.writeText(codeString);
      setCopySuccess(true);
      setTimeout(() => setCopySuccess(false), 1500);
    };

    const handleExecuteClick = async () => {
      if(!executeSuccess){
        setExecuteSuccess(true);
        handleQueryResponse(); 
      }
    }

    return {
        copySuccess,
        handleCopyClick,
        executeSuccess,
        query,
        handleQueryChange,
        handleExecuteClick
    }
}

export default useCodeBlockViewController;