import { ReactElement, useReducer } from "react";
import reducer from "./reducer";
import QueryResultContext from "./queryResultContext";

type QueryResultProviderProps = {
    result: QueryResult;
    children: ReactElement;
}

export default function QueryResultProvider({ result, children }: QueryResultProviderProps) {
    const [state, dispatch] = useReducer(reducer, {
        queryResult: result,
        currentPage: 0,
        rowsPerPage: 10,
    });

    return (
        <QueryResultContext.Provider value={{ state, dispatch }}>
            {children}
        </QueryResultContext.Provider>
    )
}