import React from "react";

type QueryResultTableProps = {
  result: QueryResult;
};

const DownloadCSV = ({ result }: QueryResultTableProps) => {
  const downloadCSV = () => {
    if (!result) return;

    const columnNames = result.column_names;
    const rows = result.rows;

    let csvContent = "data:text/csv;charset=utf-8,";
    csvContent += columnNames.join(",") + "\n";
    rows.forEach((row: any) => {
      csvContent += row.join(",") + "\n";
    });

    const encodedUri = encodeURI(csvContent);
    const link = document.createElement("a");
    link.setAttribute("href", encodedUri);
    const time = new Date().getTime();
    link.setAttribute("download", `query_result${time}.csv`);
    document.body.appendChild(link);
    link.click();
  };

  return <button className="text-white bg-blue-500 rounded-lg hover:text-black hover:bg-white border px-4 py-2" onClick={downloadCSV}>Download CSV</button>;
};

export default DownloadCSV;
