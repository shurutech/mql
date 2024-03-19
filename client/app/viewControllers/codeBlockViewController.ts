import { useState } from "react";

type Props = {
    codeString: string;
  };

const useCodeBlockViewController = ({codeString}: Props) => {
    const [copySuccess, setCopySuccess] = useState(false);

    const handleCopyClick = () => {
      navigator.clipboard.writeText(codeString);
      setCopySuccess(true);
      setTimeout(() => setCopySuccess(false), 1500);
    };

    return {
        copySuccess,
        handleCopyClick,
    }
}

export default useCodeBlockViewController;