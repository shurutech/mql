"use client";

import Link from "next/link";
import useGenericViewController from "../viewControllers/genericViewController";
import { log } from "console";
import appText from "../assets/strings";

const Navbar = () => {
  const {
    logout
  } = useGenericViewController();

  const text = appText.headerNavbar;

  return (
    <div className="bg-gray-100">
      <header className="bg-white shadow-md">
        <div className="mx-auto max-w-6xl px-4 sm:px-6 lg:px-8">
          <div className="container mx-auto px-4 py-2 flex items-center justify-between">
            <div className="flex items-center">
              <img src="/MQLAI.png" alt="Logo" className="w-34 h-10 mb-1" />
              <nav className="ml-6">
                <Link href="/home">
                  <span className="text-gray-600 font-bold hover:text-gray-900 hover:underline px-3 py-2">
                    {text.home}
                  </span>
                </Link>
              </nav>
            </div>
            <div className="flex items-center">
              <div>
                <Link
                  href="/add-database"
                  className="text-white bg-blue-500 rounded-full hover:text-black hover:bg-white border px-4 py-2"
                >
                  {text.addDatabase}
                </Link>
                <button
                  className="text-gray-600 hover:text-gray-900 px-3 py-2"
                  onClick={logout}
                >
                  {text.logout}
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
