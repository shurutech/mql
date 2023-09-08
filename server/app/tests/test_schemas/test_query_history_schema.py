import pytest
from pydantic import ValidationError
from uuid import uuid4
from app.schemas.query_history import QueryHistory as QueryHistorySchema


def test_query_history_schema_with_valid_data() -> None:
    nl_query = "What is the total sales for the month of January?"
    sql_query = "SELECT SUM(sales) FROM sales WHERE month = 'January'"
    user_database_id = uuid4()
    id = uuid4()
    query_history = QueryHistorySchema(
        id=id, nl_query=nl_query, sql_query=sql_query, user_database_id=user_database_id
    )
    assert query_history.nl_query == nl_query
    assert query_history.sql_query == sql_query
    assert query_history.user_database_id == user_database_id
    assert query_history.id == id


def test_query_history_schema_with_invalid_nl_query() -> None:
    with pytest.raises(ValidationError):
        nl_query = 1
        sql_query = "SELECT SUM(sales) FROM sales WHERE month = 'January'"
        user_database_id = uuid4()
        QueryHistorySchema(
            nl_query=nl_query,
            sql_query=sql_query,
            user_database_id=user_database_id,
        )


def test_query_history_schema_with_invalid_sql_query() -> None:
    with pytest.raises(ValidationError):
        nl_query = "What is the total sales for the month of January?"
        sql_query = 1
        user_database_id = uuid4()
        QueryHistorySchema(
            nl_query=nl_query,
            sql_query=sql_query,
            user_database_id=user_database_id,
        )


def test_query_history_schema_with_invalid_user_database_id() -> None:
    with pytest.raises(ValidationError):
        nl_query = "What is the total sales for the month of January?"
        sql_query = "SELECT SUM(sales) FROM sales WHERE month = 'January'"
        user_database_id = "1"
        QueryHistorySchema(
            nl_query=nl_query,
            sql_query=sql_query,
            user_database_id=user_database_id,
        )


def test_query_history_schema_with_invalid_id() -> None:
    with pytest.raises(ValidationError):
        nl_query = "What is the total sales for the month of January?"
        sql_query = "SELECT SUM(sales) FROM sales WHERE month = 'January'"
        user_database_id = uuid4()
        id = "1"
        QueryHistorySchema(
            nl_query=nl_query,
            sql_query=sql_query,
            user_database_id=user_database_id,
            id=id,
        )


def test_query_history_schema_with_missing_nl_query() -> None:
    with pytest.raises(ValidationError):
        sql_query = "SELECT SUM(sales) FROM sales WHERE month = 'January'"
        user_database_id = uuid4()
        QueryHistorySchema(
            sql_query=sql_query,
            user_database_id=user_database_id,
        )


def test_query_history_schema_with_missing_user_database_id() -> None:
    with pytest.raises(ValidationError):
        nl_query = "What is the total sales for the month of January?"
        sql_query = "SELECT SUM(sales) FROM sales WHERE month = 'January'"
        QueryHistorySchema(
            nl_query=nl_query,
            sql_query=sql_query,
        )


def test_query_history_schema_with_missing_sql_query() -> None:
    nl_query = "What is the total sales for the month of January?"
    user_database_id = uuid4()
    query_history = QueryHistorySchema(
        nl_query=nl_query, user_database_id=user_database_id
    )
    assert query_history.nl_query == nl_query
    assert query_history.sql_query is None
    assert query_history.user_database_id == user_database_id
    assert query_history.id is None


def test_query_history_schema_with_missing_id() -> None:
    nl_query = "What is the total sales for the month of January?"
    sql_query = "SELECT SUM(sales) FROM sales WHERE month = 'January'"
    user_database_id = uuid4()
    query_history = QueryHistorySchema(
        nl_query=nl_query, sql_query=sql_query, user_database_id=user_database_id
    )
    assert query_history.nl_query == nl_query
    assert query_history.sql_query == sql_query
    assert query_history.user_database_id == user_database_id
    assert query_history.id is None
