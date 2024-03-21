import Image from "next/image";
import Header from "@/app/components/header";
import useHomeViewController from "./viewControllers/homeViewController";

const Home = () => {

  const {
    features,
    setupSteps,
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
              <div className="mx-auto max-w-2xl text-center sm:mt-40 mb-20">
                <h1 className="text-4xl font-bold tracking-tight text-gray-900 sm:text-6xl text-transparent bg-clip-text bg-gradient-to-t from-[#1D85FF] to-[#1106A8]">
                  Unleash the true potential of your data today!
                </h1>
                <p className="mt-6 text-lg leading-8 text-gray-600">
                  Experience effortless data exploration on our Platform, where
                  you can ask questions in plain English and instantly receive
                  AI-driven insights along with the corresponding SQL queries.
                </p>
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

        <div id="steps" className="mx-auto max-w-7xl px-6 lg:px-8 pt-28 mb-20">
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
      </main>
    </div>
  );
};

export default Home;
