import { useContext } from "react";
import QueryResultContext from "../providers/queryResultProvider/queryResultContext";

export default function useQueryResultViewController() {
    const context = useContext(QueryResultContext);

    if(!context) {
        throw new Error('useQueryResult must be used within a QueryResultProvider');
    }

    const { state, dispatch } = context;

    const { queryResult, currentPage, rowsPerPage } = state;

    const startIndex = currentPage * rowsPerPage;
    const endIndex = startIndex + rowsPerPage;
    const paginatedRows = queryResult.rows.slice(startIndex, endIndex);

    return {
        columns: queryResult.column_names,
        rows: paginatedRows,
        currentPage,
        rowsPerPage,
        totalRows: queryResult.rows.length,
        setPage: (page: number) => dispatch({ type: 'SET_PAGE', payload: page }),
        setRowsPerPage: (rowsPerPage: number) => dispatch({ type: 'SET_ROWS_PER_PAGE', payload: rowsPerPage }),
    };
};