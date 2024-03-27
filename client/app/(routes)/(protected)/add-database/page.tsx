// Use client directive indicates this file should only run in the client-side environment.
"use client";
import Image from "next/image";
import useAddDatabaseViewController from "@/app/viewControllers/addDatabaseViewController";
import appText from "@/app/assets/strings";
import DatabaseConnector from "@/app/components/databaseConnector";
import UploadDatabaseSchema from "@/app/components/schemaUploader";



const AddDatabase = () => {
  const {
    isConnectVisible,
    toggleComponent
  } = useAddDatabaseViewController();

  const text = appText.addDatabase;

  return (
    <div className="mx-auto max-w-6xl px-4 sm:px-6 lg:px-8">
      <div className="flex flex-col gap-8 md:flex-row mt-8">
        <div className="my-auto w-full md:w-1/2">
          <div className="w-4/5">
            <p className="text-3xl font-bold text-[#2b4499]">{text.title}</p>
            <p className="text-2xl mt-8 text-[#0a2355]">
              {text.description} <br />
            </p>
          </div>
        </div>
        <div className="flex my-auto align-middle justify-center w-full md:w-1/2">
          <Image
            src="/database_3.jpg"
            alt="database"
            className="items-center"
            width={700}
            height={700}
          />
        </div>
      </div>
      <div className="container mx-auto py-8 px-4">
        {isConnectVisible ? (
          <DatabaseConnector onToggle={toggleComponent} />
        ) : (
          <UploadDatabaseSchema onToggle={toggleComponent} />
        )}
      </div>
    </div>
  );
};

export default AddDatabase;
