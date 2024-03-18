"use client";

import { useRouter } from "next/navigation";
import { useState } from "react";
import { toast } from "react-toastify";
import { login } from "@/lib/service";
import Cookies from "js-cookie";
import Header from "@/app/components/header";

const Login = () => {
  const [email, setEmail] = useState<string>("");
  const [password, setPassword] = useState<string>("");

  const { push } = useRouter();

  const handleLogin = async (e: React.ChangeEvent<any>) => {
    e.preventDefault();
    try {
      const formData = new FormData();
      formData.append("email", email);
      formData.append("password", password);
      const res = await login(formData);
      if (res.status === 200) {
        Cookies.set("token", res.headers["x-auth-token"]);
        toast.success("Login successful");
        push("/accounts/home");
      }
    } catch (error: any) {
      toast.error(error.detail);
    }
  };

  return (
    <>
      <Header token={""} />
      <div className="min-h-screen flex items-center justify-center bg-gray-100">
        <div className="max-w-md w-full bg-white p-8 shadow-md rounded-lg">
          <h2 className="text-2xl font-bold mb-6">Login</h2>
          <form>
            <div className="mb-4">
              <label
                className="block text-gray-700 text-sm font-bold mb-2"
                htmlFor="email"
              >
                Email
              </label>
              <input
                className="w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring focus:border-blue-300"
                type="email"
                name="email"
                id="email"
                placeholder="Enter your email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
              />
            </div>
            <div className="mb-6">
              <label
                className="block text-gray-700 text-sm font-bold mb-2"
                htmlFor="password"
              >
                Password
              </label>
              <input
                className="w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring focus:border-blue-300"
                type="password"
                name="password"
                id="password"
                placeholder="Enter your password"
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
              Login
            </button>
          </form>
          {/* <p className="mt-4 text-sm text-gray-600">
          Don't have an account?{" "}
          <Link href="/signup">
            <span className="text-blue-500 underline">Signup here</span>
          </Link>
        </p> */}
        </div>
      </div>
    </>
  );
};

export default Login;
