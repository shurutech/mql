import { ArrowPathIcon, TrashIcon } from "@heroicons/react/24/solid";
import { handleDate } from "@/app/utils/helper";
import Link from "next/link";
import appText from "@/app/assets/strings";
import useDatabaseCardViewController from "../viewControllers/databaseCardViewController";
import React from "react";

type Database = {
    id: string;
    name: string;
    connection_string: boolean;
    created_at: string;
};
type Props = {
    db: Database;
    refreshDatabases: () => void;
};

const DatabaseCard = ({ db,refreshDatabases }: Props):React.JSX.Element =>{
    const text = appText.homeDatabases;
    const { syncDbLoader, syncDb, deleteDb, deleteDbLoader} = useDatabaseCardViewController(db.id, refreshDatabases);
    return (
        <div
        className="flex flex-col gap-6 border rounded-3xl shadow p-4"
      >
        <div className="flex justify-between">
          <p className="text-lg font-semibold">{db.name}</p>
          <div className="flex gap-2">

          {db.connection_string && <div className="flex justify-center items-center h-full ">
            <div className={syncDbLoader ? "animate-spin" : ""} onClick={syncDb}>
              <ArrowPathIcon className="h-6 aspect-square m-auto text-black " />
            </div>
          </div>}
          <div className={deleteDbLoader ? "animate-pulse": ""} onClick={deleteDb}>
            <TrashIcon className="h-6 cursor-pointer text-red-500" />
          </div>
          </div>
        </div>
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
              href={`/query?db_id=${db.id}`}
              className="flex-grow rounded-full bg-blue-300 px-4 py-1"
              onClick={() => 
                {
                  localStorage.setItem("selectedDb", db.name)
                  localStorage.setItem("selectedDbExecutable", JSON.stringify(db.connection_string))
                }
              }  
            >
              {text.askQuery}
            </Link>
          </div>
        </div>
      </div>
    )
}
export default DatabaseCard;