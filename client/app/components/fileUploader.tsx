import Image from "next/image";
import appText from "../assets/strings";
import React from "react";

type Props = {
  file: File | null;
  handleFileChange: (e: React.ChangeEvent<any>) => void;
  databaseName: string;
  handleUpload: () => void;
  setDatabaseName: (name: string) => void;
  showLoader: boolean;
};

const FileUploader = ({
  file,
  handleFileChange,
  databaseName,
  handleUpload,
  setDatabaseName,
  showLoader,
}: Props):React.JSX.Element => {

  const text = appText.uploadDatabaseSchema;

  return (
    <div className="bg-white border border-gray-300 rounded-md p-4 shadow-md">
      <div>
        <label className="block mb-2 font-semibold text-gray-800">
          {text.chooseFileTitle}
        </label>
        <input type="file" className="mb-4" onChange={handleFileChange} />
      </div>
      <div>
        <label className="block mb-2 font-semibold text-gray-800">
          {text.databaseName}
        </label>
        <input
          type="text"
          value={databaseName}
          onChange={(e) => setDatabaseName(e.target.value)}
          className="mb-4 border border-gray-300 px-4 py-2 rounded-full"
        />
      </div>

      <div className="flex flex-row gap-4">
        <button
          onClick={handleUpload}
          disabled={!file || !databaseName}
          className="bg-blue-500 text-white font-semibold py-1 px-4 rounded-full disabled:bg-blue-500 disabled:text-white disabled:opacity-75 hover:bg-white border-2 border-white hover:border-gray-200 hover:text-black"
        >
          {text.upload}
        </button>
        {showLoader && (
          <Image src="/loading.gif" alt="loading" width={35} height={20} />
        )}
      </div>
    </div>
  );
};

export default FileUploader;
