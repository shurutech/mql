import { useState } from "react";
import { syncSchema } from "@/app/lib/service";
import { toast } from "react-toastify";

const useDatabaseCardViewController = (id: string) => {
  const [syncDbLoader, setSyncDbLoader] = useState<boolean>(false);
  const syncDb = async () => {
    setSyncDbLoader(true);
    const formData = new FormData();
    formData.append("database_id", id);
    try {
      await syncSchema(formData);
      toast.success("Database synced successfully");
    } catch (error) {
      toast.error("Error syncing database");
    }
    setSyncDbLoader(false);
  };
  return { syncDbLoader, syncDb };
};
export default useDatabaseCardViewController;
