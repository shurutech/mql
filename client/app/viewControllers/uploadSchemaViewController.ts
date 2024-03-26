import { useState } from "react";
import { useRouter } from "next/navigation";
import { toast } from "react-toastify";
import { uploadSchema } from "@/app/lib/service";
import appText from "../assets/strings";

const useUploadSchemaViewController = () => {
  const [file, setFile] = useState<any>(null);
  const [databaseName, setDatabaseName] = useState("");
  const [showLoader, setShowLoader] = useState(false);

  const { push } = useRouter();

  const handleFileChange = (event: React.ChangeEvent<any>) => {
    const selectedFile = event.target.files[0];
    setFile(selectedFile);
  };

  const handleUpload = async () => {
    setShowLoader(true);
    try {
      const formData = new FormData();
      formData.append("database_name", databaseName);
      formData.append("file", file);

      const res = await uploadSchema(formData);
      toast.success(appText.toast.uploadSuccess);
      push("/accounts/home");
      setShowLoader(false);
    } catch (error) {
      setShowLoader(false);
      toast.error(appText.toast.errGeneric);
    }
  };

  return {
    file,
    setFile,
    databaseName,
    setDatabaseName,
    showLoader,
    setShowLoader,
    handleFileChange,
    handleUpload,
  }

}

export default useUploadSchemaViewController;