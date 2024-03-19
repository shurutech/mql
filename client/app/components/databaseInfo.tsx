"use client";

import { ChevronLeftIcon, ChevronRightIcon } from "@heroicons/react/20/solid";
import Link from "next/link";
import Accordion from "./accordion";
import useDatabaseInfoViewController from "../viewControllers/databaseInfoViewController";

type Database = {
  database: {
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
};

const DatabaseInfo = ({ database }: Database) => {
  const {
    activeIndex,
    handleAccordionToggle,
  } = useDatabaseInfoViewController();
  return (
    <div className="mx-auto max-w-6xl px-4 sm:px-6 lg:px-8 mt-8">
      <div className="mb-6">
        <div>
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
                    Database Detail
                  </Link>
                </div>
              </li>
            </ol>
          </nav>
        </div>
        <div className="mt-6 md:flex md:items-center md:justify-between">
          <div className="min-w-0 flex-1">
            <h2 className="text-2xl font-bold leading-7 text-gray-900 sm:truncate  sm:tracking-tight">
              {database.database_name}
            </h2>
            <hr
              className="mt-2 w-full border-t border-gray-300"
              aria-hidden="true"
            />
          </div>
        </div>
      </div>

      <div>
        <label className="text-gray-500 text-sm">Description</label>
        <h1 className="text-[16px]">
          This database has {database.database_tables?.length} tables.
        </h1>
      </div>
      <div className="my-8">
        <p className="font-semibold text-xl">Table Info</p>
        <hr
          className="mt-2 w-full border-t border-gray-300"
          aria-hidden="true"
        />
      </div>

      <Accordion
        activeIndex={activeIndex}
        handleAccordionToggle={handleAccordionToggle}
        tables={database.database_tables}
      />
    </div>
  );
};

export default DatabaseInfo;
