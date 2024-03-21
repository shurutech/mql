import { Fragment, useState } from "react";
import { Dialog, Transition } from "@headlessui/react";
import { XMarkIcon } from "@heroicons/react/24/outline";
import { handleDate } from "@/app/utils/helper";
import appText from "../assets/strings";

type Props = {
  open: boolean;
  setOpen: (open: boolean) => void;
  queryHistoryList: any[];
  getQueryHistory: (id: string) => void;
};

const QueryHistory = ({
  open,
  setOpen,
  queryHistoryList,
  getQueryHistory,
}: Props) => {
  return (
    <Transition.Root show={open} as={Fragment}>
      <Dialog as="div" className="relative z-10" onClose={setOpen}>
        <Transition.Child
          as={Fragment}
          enter="ease-out duration-300"
          enterFrom="opacity-0"
          enterTo="opacity-100"
          leave="ease-in duration-200"
          leaveFrom="opacity-100"
          leaveTo="opacity-0"
        >
          <div className="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity" />
        </Transition.Child>

        <div className="fixed inset-0 z-10">
          <div className="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0">
            <Transition.Child
              as={Fragment}
              enter="ease-out duration-300"
              enterFrom="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95"
              enterTo="opacity-100 translate-y-0 sm:scale-100"
              leave="ease-in duration-200"
              leaveFrom="opacity-100 translate-y-0 sm:scale-100"
              leaveTo="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95"
            >
              <Dialog.Panel className=" transform max-h-[600px] overflow-hidden rounded-lg bg-white px-4 pb-4 pt-5 text-left shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-2xl sm:p-6">
                <div className="flex justify-between">
                  <Dialog.Title
                    as="h3"
                    className="text-lg leading-6 font-medium text-gray-900"
                  >
                    {appText.chatInterface.queryHistory}
                  </Dialog.Title>
                  <button
                    type="button"
                    className="bg-white rounded-md text-gray-400 hover:text-gray-500 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500"
                    onClick={() => setOpen(false)}
                  >
                    <span className="sr-only">Close</span>
                    <XMarkIcon className="h-6 w-6" aria-hidden="true" />
                  </button>
                </div>
                <div className="mt-2">
                  <p className="text-sm text-gray-500">
                    {appText.chatInterface.queryHistoryDescription}
                  </p>
                </div>
                <div className="overflow-y-scroll max-h-[26rem] mt-4 custom-scrollbar">
                  <ul className="divide-y divide-gray-200">
                    {queryHistoryList.length ? (
                      queryHistoryList?.map((query, idx) => (
                        <li
                          key={idx}
                          className="py-4 px-2 hover:bg-gray-200 cursor-pointer"
                          onClick={() => {
                            getQueryHistory(query.id);
                            setOpen(false);
                          }}
                        >
                          <div className="flex space-x-3">
                            <div className="flex-1 space-y-1">
                              <div className="flex gap-4 items-center justify-between">
                                <h3 className="text-md font-medium">
                                  {query.nl_query}
                                </h3>
                                <h3 className="text-sm text-gray-500">
                                  {handleDate(query.created_at)}
                                </h3>
                              </div>
                            </div>
                          </div>
                        </li>
                      ))
                    ) : (
                      <p className="text-center my-4">
                        No query history found.
                      </p>
                    )}
                  </ul>
                </div>
              </Dialog.Panel>
            </Transition.Child>
          </div>
        </div>
      </Dialog>
    </Transition.Root>
  );
};

export default QueryHistory;
