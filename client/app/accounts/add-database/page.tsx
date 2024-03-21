"use client";

import CodeBlock from "@/app/components/codeBlock";
import FileUploader from "@/app/components/fileUploader";
import { COMMAND_RUN_SCRIPT, COMMAND_DOWNLOAD_SCRIPT } from "@/app/utils/constant";
import Image from "next/image";
import useAddDatabaseViewController from "@/app/viewControllers/addDatabaseViewController";
import appText from "@/app/assets/strings";

const AddDatabase = () => {
  const {
    file,
    databaseName,
    setDatabaseName,
    showLoader,
    handleFileChange,
    handleUpload,
  } = useAddDatabaseViewController();

  const text = appText.addDatabase;
  
  return (
    <div className="mx-auto max-w-6xl px-4 sm:px-6 lg:px-8">
      <div className="flex flex-col gap-8 md:flex-row mt-8">
        <div className="my-auto w-full md:w-1/2">
          <div className="w-4/5">
            <p className="text-3xl font-bold text-[#2b4499]">
              {text.title}
            </p>
            <p className="text-2xl mt-8 text-[#0a2355]">
              {text.description} <br />{" "}
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
      <div>
        <div className="mt-8">
          <h2 className="text-4xl font-bold mb-6">{text.steps}</h2>
        </div>
        <ul role="list" className="space-y-3">
          <li className="overflow-hidden bg-orange-50 px-4 pt-8 pb-4 shadow sm:rounded-md sm:px-6">
            <div>
              <p className="text-lg">
                {text.firstStep}
              </p>
              <div className="container mx-auto py-8 px-4">
                <CodeBlock codeString={COMMAND_DOWNLOAD_SCRIPT} language="bash" />
              </div>
            </div>
            <div>
              <p className="text-lg">
                {text.secondStep}
              </p>
              <div className="container mx-auto py-8 px-4">
                <CodeBlock codeString={COMMAND_RUN_SCRIPT} language="bash" />
              </div>
            </div>
            <div>
              <p className="text-lg">
                {text.thirdStep}
              </p>
              <div className="container mx-auto py-8 px-4">
                <FileUploader
                  file={file}
                  handleFileChange={handleFileChange}
                  databaseName={databaseName}
                  handleUpload={handleUpload}
                  setDatabaseName={setDatabaseName}
                  showLoader={showLoader}
                />
              </div>
            </div>
          </li>
        </ul>
      </div>
    </div>
  );
};

export default AddDatabase;
