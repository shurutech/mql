"use client";

import Link from "next/link";
import { handleDate } from "@/app/utils/helper";
import useHomeAccountsViewController  from "@/app/viewControllers/homeAccountsViewController";
import appText from "@/app/assets/strings";

const Home = () => {

  const {
    databases
  } = useHomeAccountsViewController();

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
            <div
              key={idx}
              className="flex flex-col gap-6 border rounded-3xl shadow p-4"
            >
              <p className="text-lg font-semibold">{db.name}</p>
              <div className="flex flex-col gap-3">
                <p className="text-gray-500 text-sm text-right">
                  {text.added} {handleDate(db.created_at)}
                </p>
                <div className="flex flex-row text-center w-full gap-4">
                  <Link
                    href={`/databases/${db.id}`}
                    className="flex-grow rounded-full border hover:bg-blue-300 px-4 py-1"
                  >
                    {text.viewDb}
                  </Link>
                  <Link
                    href={`/query/${db.id}`}
                    className="flex-grow rounded-full bg-blue-300 px-4 py-1"
                    onClick={() => localStorage.setItem("selectedDb", db.name)}
                  >
                    {text.askQuery}
                  </Link>
                </div>
              </div>
            </div>
          ))
        ) : (
          <p>{text.noDatabase}</p>
        )}
      </div>
    </div>
  );
};

export default Home;
