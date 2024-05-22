type DataValue = string | number | boolean;

type Column = string;

type Row = DataValue[];

type QueryResult = {
    column_names: Column[];
    rows: Row[];
};

type Action = { type: 'SET_RESULT'; payload: QueryResult } 
    | { type: 'SET_PAGE'; payload: number } 
    | { type: 'SET_ROWS_PER_PAGE'; payload: number };

type QueryResultState = {
    queryResult: QueryResult;
    currentPage: number;
    rowsPerPage: number;
};

