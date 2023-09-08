import { ChevronDownIcon, ChevronUpIcon } from "@heroicons/react/20/solid";

type Props = {
  tables: {
    table_id: string;
    table_name: string;
    table_columns: {
      column_id: string;
      column_name: string;
      column_type: string;
    }[];
  }[];
  activeIndex: number | null;
  handleAccordionToggle: (idx: number) => void;
};

const Accordion = ({ tables, activeIndex, handleAccordionToggle }: Props) => {
  return (
    <div>
      <ul
        role="list"
        className="divide-y divide-gray-100 overflow-hidden bg-white shadow-sm ring-1 ring-gray-900/5 sm:rounded-xl"
      >
        {tables &&
          tables.map((table, idx) => (
            <div key={idx}>
              <li
                className="relative px-4 py-5 hover:bg-gray-50 sm:px-6 cursor-pointer"
                onClick={() => handleAccordionToggle(idx)}
              >
                <div className="flex justify-between gap-x-6">
                  <div className="min-w-0 flex-auto">
                    <p className=" font-medium leading-6 text-gray-900">
                      <span className="absolute inset-x-0 -top-px bottom-0" />
                      {idx + 1}. {table.table_name}
                    </p>
                  </div>
                  <div className="flex shrink-0 items-center gap-x-4">
                    <div className="hidden sm:flex sm:flex-col sm:items-end">
                      <p className="text-sm leading-6 text-gray-900">
                        {table.table_columns.length} columns
                      </p>
                    </div>
                    <ChevronDownIcon
                      className={`h-5 w-5 flex-none text-gray-400 transition ease-in-out duration-500 ${
                        activeIndex === idx ? "transform: rotate-180" : ""
                      }`}
                      aria-hidden="true"
                    />
                  </div>
                </div>
              </li>

              <div
                className={`${
                  activeIndex === idx
                    ? "py-2 max-h-full opacity-100"
                    : "max-h-0 opacity-0"
                } px-4 transition-all duration-300`}
              >
                <div className="-mx-4 overflow-x-auto sm:-mx-6 lg:-mx-8 px-6">
                  <div className="inline-block min-w-full align-middle shadow ring-1 ring-black ring-opacity-5 sm:rounded-lg sm:px-6 lg:px-8 bg-gray-100">
                    <table className="min-w-full divide-y divide-gray-300">
                      <thead>
                        <tr>
                          <th
                            scope="col"
                            className="py-3.5 pl-4 pr-3 text-left text-sm font-bold text-gray-900 sm:pl-0"
                          >
                            Column name
                          </th>
                          <th
                            scope="col"
                            className="px-3 py-3.5 text-left text-sm font-bold text-gray-900"
                          >
                            Data Type
                          </th>
                        </tr>
                      </thead>
                      <tbody className="divide-y divide-gray-300">
                        {table.table_columns &&
                          table.table_columns.map((column, id) => (
                            <tr key={id}>
                              <td className="whitespace-nowrap py-5 pl-4 pr-3 text-sm sm:pl-0">
                                <div className="">
                                  <div className="font-medium text-gray-900">
                                    {column.column_name}
                                  </div>
                                </div>
                              </td>
                              <td className="whitespace-nowrap px-3 py-5 text-sm text-gray-500">
                                <div className="text-gray-900">
                                  {column.column_type}
                                </div>
                              </td>
                            </tr>
                          ))}
                      </tbody>
                    </table>
                  </div>
                </div>
              </div>
            </div>
          ))}
      </ul>
    </div>
  );
};

export default Accordion;
