import { useState } from "react";

interface UseAddDatabaseViewController {
  isConnectVisible: boolean;
  setIsConnectVisible: React.Dispatch<React.SetStateAction<boolean>>;
  toggleComponent: () => void;
}

const useAddDatabaseViewController = (): UseAddDatabaseViewController => {

  const [isConnectVisible, setIsConnectVisible] = useState<boolean>(true);

  const toggleComponent = () => setIsConnectVisible(!isConnectVisible);

 
  return {
    isConnectVisible,
    setIsConnectVisible,
    toggleComponent
  };
};

export default useAddDatabaseViewController;
