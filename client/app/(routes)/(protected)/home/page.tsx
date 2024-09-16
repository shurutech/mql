"use client";

import useHomeAccountsViewController from "@/app/viewControllers/homeAccountsViewController";
import appText from "@/app/assets/strings";
import DatabaseCard from "@/app/components/databaseCard";
import React from "react";

const Home:React.FC = () => {
  const { databases,refreshDatabases } = useHomeAccountsViewController();
  const text = appText.homeDatabases;

  return (
    <div className="mx-auto max-w-6xl px-4 sm:px-6 lg:px-8 mt-8">
      <div className="mt-6 md:flex md:items-center md:justify-between">
        <div className="min-w-0 flex-1">
          <h2 className="text-2xl font-bold leading-7 text-gray-900 sm:truncate  sm:tracking-tight">
            {text.databases}
          </h2>
          <hr
            className="mt-2 w-full border-t border-gray-300"
            aria-hidden="true"
          />
        </div>
      </div>
      <div className="flex flex-row flex-wrap gap-x-6 gap-y-8  mt-8">
        {databases.length ? (
          databases?.map((db, idx) => (
            <DatabaseCard db={db} key={idx} refreshDatabases={refreshDatabases}/>
          ))
        ) : (
          <p>{text.noDatabase}</p>
        )}
      </div>
    </div>
  );
};

export default Home;
