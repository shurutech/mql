"use client";

import CodeBlock from "@/app/components/codeBlock";
import FileUploader from "@/app/components/fileUploader";
import { COMMAND_RUN_SCRIPT, COMMAND_DOWNLOAD_SCRIPT } from "@/app/utils/constant";
import useUploadSchemaViewController from "@/app/viewControllers/uploadSchemaViewController";
import appText from "@/app/assets/strings";
import React from "react";


const UploadDatabaseSchema = ({ onToggle }: { onToggle: any }):React.JSX.Element => {
  const {
    file,
    databaseName,
    setDatabaseName,
    showLoader,
    handleFileChange,
    handleUpload,
  } = useUploadSchemaViewController();

  const text = appText.uploadDatabaseSchema;

  return (
    <div className="mx-auto max-w-6xl px-4 sm:px-6 lg:px-8">
      <div className="mt-8">
        <div className="flex items-center mb-6">
          <div className="text-4xl font-bold">  {text.steps} </div>
          <div className="flex items-center justify-center text-xl mx-4 mt-2">
            {text.or}{' '}
            <button
              onClick={onToggle}
              className="text-blue-600 hover:text-blue-800 transition duration-300 ease-in-out underline ml-4 mx-1"
            >
              {text.connect}
            </button>
            {' '}{text.yourDatabase}
          </div>
        </div>
        <div className="text-red-500">  {text.information} </div>
        <ul role="list" className="space-y-3">
          <li className="overflow-hidden bg-orange-50 px-4 pt-8 pb-4 shadow sm:rounded-md sm:px-6">
            <div>
              <p className="text-lg">
                {text.firstStep}
              </p>
              <div className="container mx-auto py-8 px-4">
                <CodeBlock codeString={COMMAND_DOWNLOAD_SCRIPT} setSql={()=>null} handleQueryResponse={()=>null} executeFlag={false}/>
              </div>
            </div>
            <div>
              <p className="text-lg">
                {text.secondStep}
              </p>
              <div className="container mx-auto py-8 px-4">
                <CodeBlock codeString={COMMAND_RUN_SCRIPT}  setSql={()=>null} handleQueryResponse={()=>null} executeFlag={false}/>
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

export default UploadDatabaseSchema;
