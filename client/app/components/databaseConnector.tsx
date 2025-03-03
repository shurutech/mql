// Use client directive indicates this file should only run in the client-side environment.
"use client";
import useConnectDatabaseViewController from "@/app/viewControllers/connectDatabaseViewController";
import appText from "@/app/assets/strings";
import Loader from "./loader";
import React from "react";
import { useState } from "react";
import Image from "next/image";

const DatabaseConnector = ({ onToggle,titleRef }: { onToggle: any,titleRef:React.LegacyRef<HTMLDivElement> }):React.JSX.Element => {
  const {
    databaseName,
    setDatabaseName,
    databaseUser,
    setDatabaseUser,
    databasePassword,
    setDatabasePassword,
    databaseHost,
    setDatabaseHost,
    databasePort,
    setDatabasePort,
    showLoader,
    handleConnectDatabase,
  } = useConnectDatabaseViewController();

  const text = appText.connectDatabase;

  const [showPassword, setShowPassword] = useState<boolean>(false);

  return (
    <div className="mx-auto max-w-6xl px-4 sm:px-6 lg:px-8">
      <div className="mt-8">
        <div className="flex items-center  mb-6" ref={titleRef}>
          <div className="text-4xl font-bold">  {text.title} </div>
          <div className="flex items-center justify-center text-xl mx-4 mt-2">
            {text.or}{" "}
            <button
              onClick={onToggle}
              className="text-blue-600 hover:text-blue-800 transition duration-300 ease-in-out underline ml-4 mx-1"
            >
              {text.upload}
            </button>{" "}
            {text.yourDatabaseSchema}
          </div>
        </div>
        <div className="text-sm my-4"> {text.connectionString} </div>
        <div className="text-red-500"> {text.information} </div>
        <div className="overflow-hidden bg-orange-50 px-4 pt-8 pb-4 shadow sm:rounded-md sm:px-6">
          <div>
            <p className="text-lg">{text.description}</p>
            <div className="container mx-auto py-8 px-4">
              <form onSubmit={handleConnectDatabase}>
                <div className="grid grid-cols-1 gap-6">
                  <label className="block">
                    <span className="text-gray-700">{text.databaseName}</span>
                    <input
                      type="text"
                      value={databaseName}
                      onChange={(e) => setDatabaseName(e.target.value)}
                      className="mt-1 py-2 pl-2 block w-full rounded-md border-gray-300 shadow-sm"
                      placeholder={text.namePlaceholder}
                    />
                  </label>
                  <label className="block">
                    <span className="text-gray-700">{text.databaseUser}</span>
                    <input
                      type="text"
                      value={databaseUser}
                      onChange={(e) => setDatabaseUser(e.target.value)}
                      className="mt-1 py-2 pl-2 block w-full rounded-md border-gray-300 shadow-sm"
                      placeholder={text.userPlaceholder}
                    />
                  </label>
                  <label className="block">
                    <span className="text-gray-700">
                      {text.databasePassword}
                    </span>
                    <div className="relative mt-1">
                      <input
                        type={showPassword ? 'text' : 'password'}
                        value={databasePassword}
                        onChange={(e) => setDatabasePassword(e.target.value)}
                        className="mt-1 py-2 pl-2 block w-full rounded-md border-gray-300 shadow-sm"
                        placeholder={text.passwordPlaceholder}
                      />
                      <span className="absolute inset-y-0 right-0 pr-2 flex items-center cursor-pointer" onClick={() => setShowPassword(!showPassword)}>
                        <Image
                          src={`/eye_${showPassword ? 'close' : 'open'}.png`}
                          alt="eye-open"
                          className="items-center"
                          width={20}
                          height={20}
                        />
                      </span>
                    </div>
                  </label>
                  <label className="block">
                    <span className="text-gray-700">{text.databaseHost}</span>
                    <input
                      type="text"
                      value={databaseHost}
                      onChange={(e) => setDatabaseHost(e.target.value)}
                      className="mt-1 py-2 pl-2 block w-full rounded-md border-gray-300 shadow-sm"
                      placeholder={text.hostPlaceholder}
                    />
                    <span className="text-gray-600 text-sm">
                      {text.databaseHostInfo}
                    </span>
                  </label>
                  <label className="block">
                    <span className="text-gray-700">{text.databasePort}</span>
                    <input
                      type="number"
                      value={databasePort}
                      onChange={(e) => setDatabasePort(e.target.value)}
                      className="mt-1 py-2 pl-2 block w-full rounded-md border-gray-300 shadow-sm"
                      placeholder={text.portPlaceholder}
                    />
                  </label>
                  <div className="w-fit">
                   { showLoader ? <div>
                      <Loader />
                    </div>
                    :
                    <button
                      type="submit"
                      className="mt-2 px-4 py-2 border border-transparent text-sm font-medium rounded-md shadow-sm text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500"
                    >
                      {text.connect}
                    </button>}
                  </div>
                </div>
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default DatabaseConnector;
