"use client";

import {
  ArrowRightCircleIcon,
  ChevronLeftIcon,
  ChevronRightIcon,
} from "@heroicons/react/20/solid";
import Link from "next/link";
import { useState } from "react";
import CodeBlock from "./codeBlock";
import { askQuery, getQueryHistoryById, queryHistory } from "@/lib/service";
import Skeleton from "react-loading-skeleton";
import { toast } from "react-toastify";
import QueryHistory from "./queryHistory";

type Props = {
  dbId: string | string[];
};

const ChatInterface = ({ dbId }: Props) => {
  const [nlQuery, setNlQuery] = useState<string>("");
  const [showNlQuery, setShowNlQuery] = useState<string | null>(null);
  const [sql, setSql] = useState<string | null>(null);
  const [queryHistoryList, setQueryHistoryList] = useState([]);
  const [isFirst, setIsFirst] = useState<boolean>(true);
  const [open, setOpen] = useState<boolean>(false);

  const getAllQueryHistory = async () => {
    try {
      const res = await queryHistory(dbId);
      setQueryHistoryList(res.data.query_history);
    } catch (error) {
      toast.error("Something went wrong");
    }
  };

  const handleQuery = async (e: React.ChangeEvent<any>) => {
    e.preventDefault();
    try {
      setIsFirst(false);
      setSql(null);
      const formData = new FormData();
      formData.append("nl_query", nlQuery);
      const res = await askQuery(dbId, formData);
      setSql(res.data.sql_query);
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
      setSql(res.data.query_history.sql_query);
      setShowNlQuery(res.data.query_history.nl_query);
      setNlQuery("");
    } catch (error) {
      toast.error("Something went wrong");
    }
  };

  return (
    <>
      <div className="mx-auto max-w-5xl px-4 sm:px-6 lg:px-8 mt-8">
        <div className="relative mb-4 h-[86vh] ">
          <nav className="sm:hidden" aria-label="Back">
            <Link
              href="/accounts/home"
              className="flex items-center text-sm font-medium text-gray-500 hover:text-gray-700"
            >
              <ChevronLeftIcon
                className="-ml-1 mr-1 h-5 w-5 flex-shrink-0 text-gray-400"
                aria-hidden="true"
              />
              Back
            </Link>
          </nav>
          <nav className="hidden sm:flex" aria-label="Breadcrumb">
            <ol role="list" className="flex items-center space-x-4">
              <li>
                <div className="flex">
                  <Link
                    href="/accounts/home"
                    className="text-sm font-medium text-gray-500 hover:text-gray-700"
                  >
                    Home
                  </Link>
                </div>
              </li>
              <li>
                <div className="flex items-center">
                  <ChevronRightIcon
                    className="h-5 w-5 flex-shrink-0 text-gray-400"
                    aria-hidden="true"
                  />
                  <Link
                    href="#"
                    className="ml-4 text-sm font-medium text-gray-500 hover:text-gray-700"
                  >
                    Query
                  </Link>
                </div>
              </li>
            </ol>
          </nav>
          <div className="mt-6">
            <div className="flex flex-row justify-between">
              <h2 className="text-2xl font-bold leading-7 text-gray-900 sm:truncate  sm:tracking-tight">
                {localStorage.getItem("selectedDb") || <Skeleton />}
              </h2>
              <button
                className="border boreder-2 rounded-full px-4 py-1 leading-7 text-gray-900 sm:truncate  sm:tracking-tight cursor-pointer hover:bg-blue-300 "
                onClick={() => {
                  getAllQueryHistory();
                  setOpen(true);
                }}
              >
                History
              </button>
            </div>
            <div
              className={`${
                isFirst ? "max-h-0" : "max-h-[26rem] sm:max-h-[62vh]"
              } overflow-y-scroll mt-8 rounded transition-all duration-1000 shadow-custom_shadow`}
            >
              <div className="bg-gray-200 rounded-t p-6">
                <p className="text-lg font-bold">Query:</p>
                <p>{showNlQuery || <Skeleton />}</p>
              </div>
              <div className="p-6">
                <p className="text-lg font-bold ">Response:</p>
                <p>{!sql ? <Skeleton count={5} /> : null}</p>
                {sql && (
                  <div className="mt-4">
                    <CodeBlock codeString={sql} language="SQL" />
                  </div>
                )}
              </div>
            </div>
          </div>
          <div
            className={`${
              isFirst ? "bottom-3/4" : "bottom-4"
            } absolute w-full rounded transition-all duration-1000`}
          >
            <form>
              <div className="flex flex-row border border-dashed border-black rounded-full bg-white">
                <input
                  className="w-full px-4 py-2 rounded-full focus:outline-none"
                  type="text"
                  name="text"
                  id="text"
                  placeholder="Ask your query"
                  value={nlQuery}
                  onChange={(e) => {
                    setNlQuery(e.target.value);
                    setShowNlQuery(e.target.value);
                  }}
                />
                <button className="p-1" type="submit" onClick={handleQuery}>
                  <ArrowRightCircleIcon
                    className="h-8 w-8 flex-shrink-0 text-gray-400 hover:text-blue-500"
                    aria-hidden="true"
                  />
                </button>
              </div>
            </form>
          </div>
        </div>
      </div>
      <QueryHistory
        open={open}
        setOpen={setOpen}
        queryHistoryList={queryHistoryList}
        getQueryHistory={getQueryHistory}
      />
    </>
  );
};

export default ChatInterface;
