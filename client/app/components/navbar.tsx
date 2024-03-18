"use client";

import Cookies from "js-cookie";
import Link from "next/link";

const Navbar = () => {
  const handleLogout = () => {
    Cookies.set("token", "");
    window.location.href = "/";
  };

  return (
    <div className="bg-gray-100">
      <header className="bg-white shadow-md">
        <div className="mx-auto max-w-6xl px-4 sm:px-6 lg:px-8">
          <div className="container mx-auto px-4 py-2 flex items-center justify-between">
            <div className="flex items-center">
              <img src="/MQLAI.png" alt="Logo" className="w-34 h-10 mb-1" />
              <nav className="ml-6">
                <Link href="/accounts/home">
                  <span className="text-gray-600 font-bold hover:text-gray-900 hover:underline px-3 py-2">
                    Home
                  </span>
                </Link>
              </nav>
            </div>
            <div className="flex items-center">
              <div>
                <Link
                  href="/accounts/add-database"
                  className="text-white bg-blue-500 rounded-full hover:text-black hover:bg-white border px-4 py-2"
                >
                  Add Database
                </Link>
                <button
                  className="text-gray-600 hover:text-gray-900 px-3 py-2"
                  onClick={handleLogout}
                >
                  Logout
                </button>
              </div>
            </div>
          </div>
        </div>
      </header>
    </div>
  );
};

export default Navbar;
