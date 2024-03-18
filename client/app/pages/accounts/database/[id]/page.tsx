"use client";

import DatabaseInfo from "@/app/components/databaseInfo";
import { useParams } from "next/navigation";
import { useEffect, useState } from "react";
import { getDatabase } from "@/app/lib/service";
import { toast } from "react-toastify";

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

const DatabaseView = () => {
  const { id } = useParams();
  const [database, setDatabase] = useState<Database>({} as Database);

  useEffect(() => {
    const fetchDB = async () => {
      try {
        const res = await getDatabase(id);
        setDatabase(res.data.data);
      } catch (error) {
        toast.error("Something went wrong");
      }
    };
    fetchDB();
  }, []);

  return (
    <div>
      <DatabaseInfo database={database} />
    </div>
  );
};

export default DatabaseView;
