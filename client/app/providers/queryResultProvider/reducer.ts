import { SET_PAGE, SET_RESULT, SET_ROWS_PER_PAGE } from "./actions";

const reducer: React.Reducer<QueryResultState, Action> = (state, action) => {
    switch (action.type) {
        case SET_RESULT:
            return { ...state, queryResult: action.payload };
        case SET_PAGE:
            return { ...state, currentPage: action.payload };
        case SET_ROWS_PER_PAGE:
            return { ...state, rowsPerPage: action.payload, currentPage: 0 };
        default:
            return state;
    }
};

export default reducer;