"use client";

import DatabaseInfo from "@/app/components/databaseInfo";
import useDatabaseViewController from "@/app/viewControllers/databaseViewController";

const DatabaseView = () => {
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
