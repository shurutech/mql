"use client";

import DatabaseInfo from "@/app/components/databaseInfo";
import useDatabaseViewController from "@/app/viewControllers/databaseViewController";
import React from "react";



const DatabaseView:React.FC = () => {
  const {
    database
  } = useDatabaseViewController();

  return (
    <div>
      <DatabaseInfo database={database} />
    </div>
  );
};

export default DatabaseView;
