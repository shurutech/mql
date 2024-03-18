import { getAllDatabase } from "@/app/lib/service";
import { useEffect, useState } from "react";
import { toast } from "react-toastify";

type Database = {
    id: number;
    name: string;
    created_at: string;
};

const useHomeAccountsViewController = () => {
    const [databases, setDatabases] = useState<Database[]>([]);

    useEffect(() => {
        const fetchAllDB = async () => {
            try {
                const response = await getAllDatabase();
                setDatabases(response.data.data.user_databases);
            } catch (error) {
                toast.error("Something went wrong");
            }
        };
        fetchAllDB();
    }, []);

    return { databases };
}

export default useHomeAccountsViewController;