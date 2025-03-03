"use client";

import { Bars3Icon, XMarkIcon } from "@heroicons/react/24/outline";
import { Dialog } from "@headlessui/react";

import Link from "next/link";
import React from "react";

import useGenericViewController from "../viewControllers/genericViewController";
import appText from "../assets/strings";

type Props = {
  token: string | undefined;
};

const Header = ({ token }: Props):React.JSX.Element => {
  const {
    headerNavigation,
    setMobileMenuOpen,
    mobileMenuOpen,
    pathname,
  } = useGenericViewController();

  const text =  appText.header;

  return (
    <header className="mx-auto max-w-7xl px-6 lg:px-8">
      <nav className="flex items-center justify-between p-6">
        <div className="flex z-50 lg:flex-1">
          <Link href="/" className="-m-1.5 p-1.5">
            <img className="h-10 w-auto" src="/MQLAI.png" alt="logo" />
          </Link>
        </div>
        <div className="flex z-50 lg:hidden">
          <button
            type="button"
            className="-m-2.5 inline-flex items-center justify-center rounded-md p-2.5 text-gray-700"
            onClick={() => setMobileMenuOpen(true)}
          >
            <span className="sr-only">{text.openMainMenu}</span>
            <Bars3Icon className="h-6 w-6" aria-hidden="true" />
          </button>
        </div>
        <div className="hidden lg:flex lg:gap-x-12 z-50">
          {pathname !== "/login" &&
            headerNavigation.map((item) => (
              <Link
                key={item.name}
                href={item.href}
                className="text-sm font-semibold leading-6 text-gray-900"
              >
                {item.name}
              </Link>
            ))}
        </div>
        <div className="hidden lg:flex lg:flex-1 lg:justify-end z-50">
          {token ? (
            <Link
              href="/home"
              className="text-sm font-semibold leading-6 text-gray-900"
            >
              {text.dashboard} <span aria-hidden="true">&rarr;</span>
            </Link>
          ) : (
            ((pathname !== "/login") ? <Link
              href="/login"
              className="text-sm font-semibold leading-6 text-gray-900"
            >
              {text.login} <span aria-hidden="true">&rarr;</span>
            </Link> : "")
          )}
        </div>
      </nav>
      <Dialog
        as="div"
        className="lg:hidden"
        open={mobileMenuOpen}
        onClose={setMobileMenuOpen}
      >
        <div className="fixed inset-0 z-50" />
        <Dialog.Panel className="fixed inset-y-0 right-0 z-50 w-full overflow-y-auto bg-white px-12 py-6 sm:max-w-sm sm:ring-1 sm:ring-gray-900/10">
          <div className="flex items-center justify-between">
            <Link href="/" className="-m-1.5 p-1.5">
              <span className="sr-only">MQL</span>
              <img className="h-10 w-auto" src="/MQLAI.png" alt="logo" />
            </Link>
            <button
              type="button"
              className="-m-2.5 rounded-md p-2.5 text-gray-700"
              onClick={() => setMobileMenuOpen(false)}
            >
              <span className="sr-only">{text.closeMenu}</span>
              <XMarkIcon className="h-6 w-6" aria-hidden="true" />
            </button>
          </div>
          <div className="mt-6 flow-root">
            <div className="-my-6 divide-y divide-gray-500/10">
              <div className="space-y-2 py-6 z-50">
                {headerNavigation.map((item) => (
                  <a
                    key={item.name}
                    href={item.href}
                    className="-mx-3 block rounded-lg px-3 py-2 text-base font-semibold leading-7 text-gray-900 hover:bg-gray-50"
                  >
                    {item.name}
                  </a>
                ))}
              </div>
              <div className="py-6">
                <Link
                  href="/login"
                  className="-mx-3 block rounded-lg px-3 py-2.5 text-base font-semibold leading-7 text-gray-900 hover:bg-gray-50"
                >
                  {text.login}
                </Link>
              </div>
            </div>
          </div>
        </Dialog.Panel>
      </Dialog>
    </header>
  );
};

export default Header;
