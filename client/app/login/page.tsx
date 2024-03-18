"use client";

import Header from "@/app/components/header";
import useLoginViewController from "@/app/viewControllers/loginViewController";

const Login = () => {

  const {
    handleLogin,
    setEmail,
    setPassword,
    email,
    password,
  } = useLoginViewController();

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
