import { createContext } from "react";

const QueryResultContext = createContext<{
    state: QueryResultState;
    dispatch: React.Dispatch<Action>;
} | null>(null);

export default QueryResultContext;