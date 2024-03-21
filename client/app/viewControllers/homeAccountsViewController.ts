import { getAllDatabase } from "@/app/lib/service";
import { useEffect, useState } from "react";
import { toast } from "react-toastify";
import appText from "../assets/strings";

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
                toast.error(appText.toast.errGeneric);
            }
        };
        fetchAllDB();
    }, []);

    return { databases };
}

export default useHomeAccountsViewController;