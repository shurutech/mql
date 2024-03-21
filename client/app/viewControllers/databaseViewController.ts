import { useParams } from "next/navigation";
import { useEffect, useState } from "react";
import { getDatabase } from "@/app/lib/service";
import { toast } from "react-toastify";
import appText from "../assets/strings";

type Database = {
    database_id: string;
    database_name: string;
    database_tables: {
        table_id: string;
        table_name: string;
        table_columns: {
            column_id: string;
            column_name: string;
            column_type: string;
        }[];
    }[];
};

const useDatabaseViewController = () => {
    const { id } = useParams();
    const [database, setDatabase] = useState<Database>({} as Database);
  
    useEffect(() => {
      const fetchDB = async () => {
        try {
          const res = await getDatabase(id);
          setDatabase(res.data.data);
        } catch (error) {
          toast.error(appText.toast.errGeneric);
        }
      };
      fetchDB();
    }, []);

    return {
        database
    }
}

export default useDatabaseViewController;

