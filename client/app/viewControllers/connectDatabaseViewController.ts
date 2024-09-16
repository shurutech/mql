import { useState } from "react";
import { useRouter } from "next/navigation";
import { toast } from "react-toastify";
import { connectDatabase } from "@/app/lib/service";
import appText from "../assets/strings";

const useConnectDatabaseViewController = () => {
  const [databaseName, setDatabaseName] = useState<string>("");
  const [databaseUser, setDatabaseUser] = useState<string>("");
  const [databasePassword, setDatabasePassword] = useState<string>("");
  const [databaseHost, setDatabaseHost] = useState<string>("");
  const [databasePort, setDatabasePort] = useState<string>("");
  const [showLoader, setShowLoader] = useState<boolean>(false);

  const { push } = useRouter();


  const handleConnectDatabase = async (e: React.ChangeEvent<HTMLFormElement>) => {
    e.preventDefault();
    try {
      setShowLoader(true);
      const formData = new FormData();
      formData.append("database_name", databaseName);
      formData.append("database_user", databaseUser);
      formData.append("database_password", databasePassword);
      formData.append("database_host", databaseHost);
      formData.append("database_port", databasePort);
      const res = await connectDatabase(formData);
      toast.success(appText.toast.connectedSuccess);
      push("/home");
      setShowLoader(false);
    } catch (error) {
      setShowLoader(false);
      toast.error(appText.toast.errGeneric);
    }
  };

  return {
    databaseName,
    setDatabaseName,
    databaseUser,
    setDatabaseUser,
    databasePassword,
    setDatabasePassword,
    databaseHost,
    setDatabaseHost,
    databasePort,
    setDatabasePort,
    showLoader,
    setShowLoader,
    handleConnectDatabase,
  }

}

export default useConnectDatabaseViewController;