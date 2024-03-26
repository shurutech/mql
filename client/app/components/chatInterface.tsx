"use client";

import {
  ArrowRightCircleIcon,
  ChevronLeftIcon,
  ChevronRightIcon,
} from "@heroicons/react/20/solid";
import Link from "next/link";
import CodeBlock from "./codeBlock";
import Skeleton from "react-loading-skeleton";
import QueryHistory from "./queryHistory";
import useChatViewController from "../viewControllers/chatViewController";
import appText from "../assets/strings";

type Props = {
  dbId: string | string[];
};

const ChatInterface = ({ dbId }: Props) => {

  const {
    nlQuery,
    setNlQuery,
    showNlQuery,
    sql,
    queryHistoryList,
    isFirst,
    open,
    setOpen,
    getAllQueryHistory,
    handleQuery,
    getQueryHistory,
  } = useChatViewController({ dbId });

  const text = appText.chatInterface;

  return (
    <>
      <div className="mx-auto max-w-5xl px-4 sm:px-6 lg:px-8 mt-8">
        <div className="relative mb-4 h-[86vh] ">
          <nav className="sm:hidden" aria-label="Back">
            <Link
              href="/home"
              className="flex items-center text-sm font-medium text-gray-500 hover:text-gray-700"
            >
              <ChevronLeftIcon
                className="-ml-1 mr-1 h-5 w-5 flex-shrink-0 text-gray-400"
                aria-hidden="true"
              />
              {text.back}
            </Link>
          </nav>
          <nav className="hidden sm:flex" aria-label="Breadcrumb">
            <ol role="list" className="flex items-center space-x-4">
              <li>
                <div className="flex">
                  <Link
                    href="/home"
                    className="text-sm font-medium text-gray-500 hover:text-gray-700"
                  >
                    {text.home}
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
                    {text.query}
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
                {text.history}
              </button>
            </div>
            <div
              className={`${isFirst ? "max-h-0" : "max-h-[26rem] sm:max-h-[62vh]"
                } overflow-y-scroll mt-8 rounded transition-all duration-1000 shadow-custom_shadow`}
            >
              <div className="bg-gray-200 rounded-t p-6">
                <p className="text-lg font-bold">{text.queryColon}</p>
                <p>{showNlQuery || <Skeleton />}</p>
              </div>
              <div className="p-6">
                <p className="text-lg font-bold ">{text.response}</p>
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
            className={`${isFirst ? "bottom-3/4" : "bottom-4"
              } absolute w-full rounded transition-all duration-1000`}
          >
            <form>
              <div className="flex flex-row border border-dashed border-black rounded-full bg-white">
                <input
                  className="w-full px-4 py-2 rounded-full focus:outline-none"
                  type="text"
                  name="text"
                  id="text"
                  placeholder= {text.askYourQuery}
                  value={nlQuery}
                  onChange={(e) => {
                    setNlQuery(e.target.value);
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
