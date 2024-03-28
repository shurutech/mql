import { useState } from "react";
import { askQuery, getQuery, getQueries } from "@/app/lib/service";
import { toast } from "react-toastify";
import appText from "../assets/strings";

type Props = {
    dbId: string;
};

const useChatViewController = ({ dbId }: Props) => {
    const [nlQuery, setNlQuery] = useState<string>("");
    const [showNlQuery, setShowNlQuery] = useState<string | null>(null);
    const [sql, setSql] = useState<string | null>(null);
    const [queries, setQueries] = useState([]);
    const [isFirst, setIsFirst] = useState<boolean>(true);
    const [open, setOpen] = useState<boolean>(false);

    const getQueryHistory = async () => {
        try {
            const res = await getQueries(dbId);
            setQueries(res.data.data.queries);
        } catch (error) {
            toast.error(appText.toast.errGeneric);
        }
    };

    const handleQuery = async (e: React.ChangeEvent<any>) => {
        e.preventDefault();
        try {
            setIsFirst(false);
            setSql(null);
            setShowNlQuery(nlQuery);
            const formData = new FormData();
            formData.append("nl_query", nlQuery);
            formData.append("db_id", dbId);
            const res = await askQuery(formData);
            setSql(res.data.data.sql_query);
            setNlQuery("");
        } catch (error) {
            toast.error(appText.toast.errGeneric);
        }
    };

    const getQueryById = async (id: string) => {
        try {
            setIsFirst(false);
            setSql(null);
            setShowNlQuery(null);
            const res = await getQuery({ id });
            setSql(res.data.data.query.sql_query);
            setShowNlQuery(res.data.data.query.nl_query);
            setNlQuery("");
        } catch (error) {
            toast.error(appText.toast.errGeneric);
        }
    };

    return {
        nlQuery,
        setNlQuery,
        showNlQuery,
        setShowNlQuery,
        sql,
        setSql,
        isFirst,
        setIsFirst,
        open,
        setOpen,
        getQueryHistory,
        handleQuery,
        getQueryById,
        queries,
    };
};

export default useChatViewController;