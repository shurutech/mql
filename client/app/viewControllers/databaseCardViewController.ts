import { useState } from "react";
import { syncSchema, deleteDatabase } from "@/app/lib/service";
import { toast } from "react-toastify";

const useDatabaseCardViewController = (id: string, refreshDatabases: ()=> void) => {
  const [syncDbLoader, setSyncDbLoader] = useState<boolean>(false);
  const [deleteDbLoader, setDeleteDbLoader] = useState<boolean>(false);
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
  
  const deleteDb = async () => {
    setDeleteDbLoader(true);
    try{
      await deleteDatabase(id);
      toast.success("Database deleted successfully");
      refreshDatabases();
    }
    catch(error){
      toast.error("Error deleting database");
    }
    setDeleteDbLoader(false);
  };

  return { syncDbLoader, syncDb , deleteDbLoader, deleteDb};
};
export default useDatabaseCardViewController;
