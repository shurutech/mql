import { ChevronLeftIcon, ChevronRightIcon } from "@heroicons/react/24/solid";
import useQueryResult from "@/app/viewControllers/queryResultViewController";
import QueryResultProvider from "@/app/providers/queryResultProvider";

function QueryResultTableHeader() {
  const result = useQueryResult();

  return (
    <thead className="text-s  text-black uppercase bg-gray-200 d">
      <tr>
        {result.columns.map((column) => {
          return <QueryTableColumnHeading key={column} column={column} />;
        })}
      </tr>
    </thead>
  );
}

function QueryTableColumnHeading({ column }: { column: Column }) {
  return (
    <th key={column} className="px-4 py-4">
      {column}
    </th>
  );
}

type QueryResultTableRowProps = {
  values: DataValue[];
  columns: Column[];
  rowIndex: number;
};

function QueryResultTableRow({
  values,
  columns,
  rowIndex,
}: QueryResultTableRowProps) {
  return (
    <tr className="bg-white border-b ">
      {values.map((value, idx) => {
        const columnName = columns[idx];
        const id = `${columnName}-${rowIndex}`;

        return (
          <td key={id} className="overflow-scroll px-4 py-2 text-black">
            {value?.toString()}
          </td>
        );
      })}
    </tr>
  );
}

function QueryResultTableBody() {
  const result = useQueryResult();

  return (
    <tbody>
      {result.rows.map((values, rowIndex) => (
        <QueryResultTableRow
          key={rowIndex}
          values={values}
          columns={result.columns}
          rowIndex={rowIndex}
        />
      ))}
    </tbody>
  );
}

function QueryResultTablePaginationControls() {
  const { currentPage, rowsPerPage, totalRows, setPage, setRowsPerPage } =
    useQueryResult();

  const totalPages = Math.ceil(totalRows / rowsPerPage);

  const handlePrevClick = () => {
    if (currentPage > 0) {
      setPage(currentPage - 1);
    }
  };

  const handleNextClick = () => {
    if (currentPage < totalPages - 1) {
      setPage(currentPage + 1);
    }
  };

  return (
    <div className="flex m-auto">
      <div className="flex gap-0 mb-5 mr-2">
        <div className="flex items-center">
          <button
            onClick={handlePrevClick}
            disabled={currentPage === 0}
            className={`px-2 py-1 mr-1  text-gray-800 rounded ${
              currentPage === 0
                ? "cursor-not-allowed opacity-50"
                : "hover:bg-gray-200"
            }`}
          >
            <ChevronLeftIcon className="h-5 w-5" />
          </button>
          <span>
            {currentPage + 1} of {totalPages}
          </span>
          <button
            onClick={handleNextClick}
            disabled={currentPage === totalPages - 1}
            className={`ml-1 px-2 py-1  text-gray-800 rounded ${
              currentPage === totalPages - 1
                ? "cursor-not-allowed opacity-50"
                : "hover:bg-gray-200"
            }`}
          >
            <ChevronRightIcon className="h-5 w-5" />
          </button>
        </div>
        <div>
          <select
            value={rowsPerPage}
            onChange={(e) => setRowsPerPage(Number(e.target.value))}
            className="px-2 py-1 border border-gray-300 rounded"
          >
            {[10, 25, 50, 200].map((option) => (
              <option key={option} value={option}>
                {option}
              </option>
            ))}
          </select>
        </div>
      </div>
    </div>
  );
}

type QueryResultTableProps = {
  result: QueryResult;
};

export default function QueryResultTable({ result }: QueryResultTableProps) {
  return (
    <QueryResultProvider result={result}>
      <div className="flex flex-col gap-2 py-3 mb-3 ">
        <div className="relative rounded-xl border overflow-x-auto">
          <table className="w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400 whitespace-nowrap">
            <QueryResultTableHeader />
            <QueryResultTableBody />
          </table>
        </div>
        <QueryResultTablePaginationControls />
      </div>
    </QueryResultProvider>
  );
}
