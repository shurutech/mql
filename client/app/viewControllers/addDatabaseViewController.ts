import { useState } from "react";

const useAddDatabaseViewController = () => {

  const [isConnectVisible, setIsConnectVisible] = useState(true);

  const toggleComponent = () => setIsConnectVisible(!isConnectVisible);

  return {
    isConnectVisible,
    setIsConnectVisible,
    toggleComponent
  }

}

export default useAddDatabaseViewController;