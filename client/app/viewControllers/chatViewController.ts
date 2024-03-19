import CodeBlock from "@/app/components/codeBlock";
import Skeleton from "react-loading-skeleton";
import QueryHistory from "@/app/components/queryHistory";
import { useState } from "react";
import { askQuery, getQueryHistoryById, queryHistory } from "@/app/lib/service";
import { toast } from "react-toastify";

type Props = {
    dbId: string | string[];
};

const useChatViewController = ({ dbId }: Props) => {
    const [nlQuery, setNlQuery] = useState<string>("");
    const [showNlQuery, setShowNlQuery] = useState<string | null>(null);
    const [sql, setSql] = useState<string | null>(null);
    const [queryHistoryList, setQueryHistoryList] = useState([]);
    const [isFirst, setIsFirst] = useState<boolean>(true);
    const [open, setOpen] = useState<boolean>(false);

    const getAllQueryHistory = async () => {
        try {
            const res = await queryHistory(dbId);
            setQueryHistoryList(res.data.data.query_histories);
        } catch (error) {
            toast.error("Something went wrong");
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
            const res = await askQuery(dbId, formData);
            setSql(res.data.data.sql_query);
            setNlQuery("");
        } catch (error) {
            toast.error("Something went wrong");
        }
    };

    const getQueryHistory = async (id: string) => {
        try {
            setIsFirst(false);
            setSql(null);
            setShowNlQuery(null);
            const res = await getQueryHistoryById({ dbId, id });
            setSql(res.data.data.query_history.sql_query);
            setShowNlQuery(res.data.data.query_history.nl_query);
            setNlQuery("");
        } catch (error) {
            toast.error("Something went wrong");
        }
    };

    return {
        nlQuery,
        setNlQuery,
        showNlQuery,
        setShowNlQuery,
        sql,
        setSql,
        queryHistoryList,
        setQueryHistoryList,
        isFirst,
        setIsFirst,
        open,
        setOpen,
        getAllQueryHistory,
        handleQuery,
        getQueryHistory,
    };
};

export default useChatViewController;