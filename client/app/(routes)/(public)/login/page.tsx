"use client";

import Header from "@/app/components/header";
import useLoginViewController from "@/app/viewControllers/loginViewController";
import appText from "../../../assets/strings";
import React from "react";

const Login:React.FC = () => {

  const {
    handleLogin,
    setEmail,
    setPassword,
    email,
    password,
  } = useLoginViewController();

  const text = appText.login;

  return (
    <>
      <Header token={""} />
      <div className="min-h-screen flex items-center justify-center bg-gray-100">
        <div className="max-w-md w-full bg-white p-8 shadow-md rounded-lg">
          <h2 className="text-2xl font-bold mb-6">{text.login}</h2>
          <form>
            <div className="mb-4">
              <label
                className="block text-gray-700 text-sm font-bold mb-2"
                htmlFor="email"
              >
                {text.email}
              </label>
              <input
                className="w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring focus:border-blue-300"
                type="email"
                name="email"
                id="email"
                placeholder={text.enterEmail}
                value={email}
                onChange={(e) => setEmail(e.target.value)}
              />
            </div>
            <div className="mb-6">
              <label
                className="block text-gray-700 text-sm font-bold mb-2"
                htmlFor="password"
              >
                {text.password}
              </label>
              <input
                className="w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring focus:border-blue-300"
                type="password"
                name="password"
                id="password"
                placeholder={text.enterPassword}
                value={password}
                onChange={(e) => setPassword(e.target.value)}
              />
            </div>
            <button
              className="w-full bg-blue-500 text-white py-2 rounded-lg hover:bg-blue-600 focus:outline-none focus:ring focus:border-blue-300 disabled:opacity-50 disabled:hover:bg-blue-500"
              type="submit"
              onClick={handleLogin}
              disabled={!email || !password}
            >
              {text.login}
            </button>
          </form>
        </div>
      </div>
    </>
  );
};

export default Login;
