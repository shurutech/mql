import Image from "next/image";
import Link from "next/link";
import Header from "@/app/components/header";
import useHomeViewController from "./viewControllers/homeViewController";
import { cookies } from "next/headers";

const Home = () => {

  const {
    features,
    setupSteps,
    footerNavigation,
    token,
  } = useHomeViewController();

  return (
    <div className="">
      <Header token={token} />

      <main className="isolate">
        <div className="relative">
          <div
            className="absolute inset-x-0 -top-40 -z-10 transform-gpu overflow-hidden blur-3xl sm:-top-80"
            aria-hidden="true"
          >
            <div
              className="relative left-[calc(50%-11rem)] aspect-[1155/678] w-[36.125rem] -translate-x-1/2 rotate-[30deg] bg-gradient-to-tr from-[#e96e6e] to-[#55a2fa] opacity-30 sm:left-[calc(50%-30rem)] sm:w-[72.1875rem]"
              style={{
                clipPath:
                  "polygon(74.1% 44.1%, 100% 61.6%, 97.5% 26.9%, 85.5% 0.1%, 80.7% 2%, 72.5% 32.5%, 60.2% 62.4%, 52.4% 68.1%, 47.5% 58.3%, 45.2% 34.5%, 27.5% 76.7%, 0.1% 64.9%, 17.9% 100%, 27.6% 76.8%, 76.1% 97.7%, 74.1% 44.1%)",
              }}
            />
          </div>
          <div>
            <div className="mx-auto max-w-7xl px-6 lg:px-8 mt-20 lg:mt-0">
              {/* <div className="flex flex-col gap-8 md:flex-row">
                <div className="my-auto w-full md:w-1/2">
                  <div className="w-4/5">
                    <p className="text-4xl font-bold tracking-tight text-gray-900 sm:text-5xl text-transparent bg-clip-text bg-gradient-to-r from-[#1D85FF] to-[#1106A8]">
                      Unleash the true potential of your data today!
                    </p>
                    <p className="mt-6 text-xl leading-7 text-gray-600">
                      Easily upload your database schema and experience the
                      power of our AI. Empower your database interactions with
                      power of AI. <br />
                    </p>
                  </div>
                </div>
                <div className="flex mb-16 align-middle justify-center w-full md:w-1/2">
                  <Image
                    src="/database_4.png"
                    alt="database"
                    className="items-center"
                    width={700}
                    height={700}
                  />
                </div>
              </div> */}
              <div className="mx-auto max-w-2xl text-center sm:mt-40 mb-20">
                <h1 className="text-4xl font-bold tracking-tight text-gray-900 sm:text-6xl text-transparent bg-clip-text bg-gradient-to-t from-[#1D85FF] to-[#1106A8]">
                  Unleash the true potential of your data today!
                </h1>
                <p className="mt-6 text-lg leading-8 text-gray-600">
                  Experience effortless data exploration on our Platform, where
                  you can ask questions in plain English and instantly receive
                  AI-driven insights along with the corresponding SQL queries.
                </p>
                <div className="mt-10 flex items-center justify-center gap-x-6">
                  <Link
                    href="#waitlist"
                    className="rounded-md bg-mqlBlue-100 px-3.5 py-2.5 text-sm font-semibold text-white shadow-sm hover:bg-mqlBlue-80 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-mqlBlue"
                  >
                    Join Waitlist
                  </Link>
                </div>
              </div>
            </div>
          </div>
          <div
            className="absolute inset-x-0 top-[calc(100%-13rem)] -z-10 transform-gpu overflow-hidden blur-3xl sm:top-[calc(100%-30rem)]"
            aria-hidden="true"
          >
            <div
              className="relative left-[calc(50%+3rem)] aspect-[1155/678] w-[36.125rem] -translate-x-1/2 bg-gradient-to-tr from-[#ff80b5] to-[#1D85FF] opacity-30 sm:left-[calc(50%+36rem)] sm:w-[72.1875rem]"
              style={{
                clipPath:
                  "polygon(74.1% 44.1%, 100% 61.6%, 97.5% 26.9%, 85.5% 0.1%, 80.7% 2%, 72.5% 32.5%, 60.2% 62.4%, 52.4% 68.1%, 47.5% 58.3%, 45.2% 34.5%, 27.5% 76.7%, 0.1% 64.9%, 17.9% 100%, 27.6% 76.8%, 76.1% 97.7%, 74.1% 44.1%)",
              }}
            />
          </div>
        </div>

        <div id="features" className="mx-auto max-w-7xl pt-20 px-6 lg:px-8">
          <div className="mx-auto max-w-2xl lg:text-center">
            <p className="mt-2 text-3xl font-bold tracking-tight text-mqlBlue-100 sm:text-4xl">
              Features
            </p>
          </div>
          <div className="mx-auto mt-16 max-w-2xl sm:mt-20 lg:mt-24 lg:max-w-4xl">
            <dl className="grid max-w-xl grid-cols-1 gap-x-8 gap-y-10 lg:max-w-none lg:grid-cols-2 lg:gap-y-16">
              {features.map((feature) => (
                <div key={feature.name} className="relative pl-16">
                  <dt className="text-base font-semibold leading-7 text-gray-900">
                    <div className="absolute left-0 top-0 flex h-10 w-10 items-center justify-center rounded-lg bg-mqlBlue-100">
                      <feature.icon
                        className="h-6 w-6 text-white"
                        aria-hidden="true"
                      />
                    </div>
                    {feature.name}
                  </dt>
                  <dd className="mt-2 text-base leading-7 text-gray-600">
                    {feature.description}
                  </dd>
                </div>
              ))}
            </dl>
          </div>
        </div>

        <div id="integration" className="mt-32 bg-mqlBlue-100">
          <div className="mx-auto max-w-7xl px-6 lg:px-8 py-10">
            <div className="flex flex-col sm:flex-row gap-4">
              <div className="flex flex-col sm:w-1/2 gap-4">
                <p className="mt-2 text-3xl font-semibold tracking-tight text-white sm:text-4xl">
                  Integrations
                </p>
                <p className="text-white text-lg">
                  Discover a Range of Supported Platforms and Explore our
                  growing ecosystem for seamless possibilities
                </p>
              </div>
              <div className="flex sm:w-1/2 items-center align-middle mt-4">
                <div className="flex items-center gap-4 rounded-lg p-4 bg-white ">
                  <Image
                    src="/postgresql.svg"
                    alt="postgres"
                    width={40}
                    height={40}
                  />
                  <div className="text-lg font-semibold">PostgreSQL</div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div id="steps" className="mx-auto max-w-7xl px-6 lg:px-8 pt-28">
          <div className="mx-auto max-w-2xl lg:text-center">
            <p className="mt-2 text-3xl font-bold tracking-tight text-mqlBlue-100 sm:text-4xl">
              3 Simple Steps
            </p>
            <p className="mt-6 text-lg leading-8 text-gray-600">
              Streamline data insights effortlessly with MQL. Just follow 3
              simple steps for powerful results.
            </p>
          </div>
          <div className="flex sm:flex-row flex-col flex-wrap items-stretch mt-8">
            {setupSteps.map((step) => (
              <div className="sm:w-1/3 w-full p-4">
                <div className="flex flex-col  gap-4 items-stretch h-full rounded-lg border-[1.2px] border-mqlBlue-100 box-border border-b-4 p-8">
                  <div className="flex flex-row items-center gap-2">
                    <step.icon className="h-8 text-mqlBlue-100" />
                    <p className="text-lg font-semibold text-gray-900">
                      {step.name}
                    </p>
                  </div>
                  <p className="text-gray-600 ">{step.description}</p>
                </div>
              </div>
            ))}
          </div>
        </div>

        <div
          id="waitlist"
          className="bg-white mx-auto max-w-7xl px-6 lg:px-8 mt-32"
        >
          <div className="border-mqlBlue-100 border rounded-lg mx-auto grid max-w-7xl grid-cols-1 gap-10 p-10 lg:p-16 lg:grid-cols-12 lg:gap-8">
            <div className=" text-3xl font-bold tracking-tight text-gray-900 sm:text-4xl lg:col-span-7 lg:text-left text-center">
              <h2 className="inline sm:block lg:inline xl:block">
                Want to Explore our product?
                <br />
              </h2>

              <p className="inline sm:block lg:inline xl:block">
                Join the waiting list.
              </p>
            </div>
            <form className="w-full mx-auto max-w-md lg:col-span-5 lg:pt-2">
              <div className="flex sm:flex-row flex-col gap-4 gap-x-4">
                <label htmlFor="email-address" className="sr-only">
                  Email address
                </label>
                <input
                  id="email-address"
                  name="email"
                  type="email"
                  autoComplete="email"
                  required
                  className="min-w-0 flex-auto rounded-md border-0 px-3.5 py-2 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-mqlBlue-100 sm:text-sm sm:leading-6"
                  placeholder="Enter your email"
                />
                <button
                  type="submit"
                  className="flex-none rounded-md bg-mqlBlue-100 px-3.5 py-2.5 text-sm font-semibold text-white shadow-sm hover:bg-mqlBlue-80 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-mqlBlue-100"
                >
                  Add to Waitlist
                </button>
              </div>
            </form>
          </div>
        </div>
      </main>

      <footer>
        <div className="bg-mqlBlue-100 mt-32">
          <div className="text-white mx-auto max-w-7xl overflow-hidden px-6 py-20 sm:py-16 lg:px-8">
            <nav
              className="flex flex-row gap-16 justify-center"
              aria-label="Footer"
            >
              {footerNavigation.main.map((item) => (
                <div key={item.name} className="pb-6">
                  <Link
                    href={item.href}
                    className="text-sm leading-6  hover:text-gray-900"
                  >
                    {item.name}
                  </Link>
                </div>
              ))}
            </nav>
            <div className=" flex justify-center space-x-10">
              {footerNavigation.social.map((item) => (
                <Link
                  key={item.name}
                  href={item.href}
                  className=" hover:text-gray-900"
                >
                  <span className="sr-only">{item.name}</span>
                  <item.icon className="h-6 w-6" aria-hidden="true" />
                </Link>
              ))}
            </div>
            <p className="mt-10 text-center text-xs leading-5 ">
              &copy; 2023 Shuru Technologies. All rights reserved.
            </p>
          </div>
        </div>
      </footer>
    </div>
  );
};

export default Home;
