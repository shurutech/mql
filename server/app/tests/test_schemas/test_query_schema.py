import pytest
from pydantic import ValidationError
from uuid import uuid4
from app.schemas.query import Query as QuerySchema


def test_query_schema_with_valid_data() -> None:
    nl_query = "What is the total sales for the month of January?"
    sql_query = "SELECT SUM(sales) FROM sales WHERE month = 'January'"
    user_database_id = uuid4()
    id = uuid4()
    query = QuerySchema(
        id=id, nl_query=nl_query, sql_query=sql_query, user_database_id=user_database_id
    )
    assert query.nl_query == nl_query
    assert query.sql_query == sql_query
    assert query.user_database_id == user_database_id
    assert query.id == id


def test_query_schema_with_invalid_nl_query() -> None:
    with pytest.raises(ValidationError):
        nl_query = 1
        sql_query = "SELECT SUM(sales) FROM sales WHERE month = 'January'"
        user_database_id = uuid4()
        QuerySchema(
            nl_query=nl_query,
            sql_query=sql_query,
            user_database_id=user_database_id,
        )


def test_query_schema_with_invalid_sql_query() -> None:
    with pytest.raises(ValidationError):
        nl_query = "What is the total sales for the month of January?"
        sql_query = 1
        user_database_id = uuid4()
        QuerySchema(
            nl_query=nl_query,
            sql_query=sql_query,
            user_database_id=user_database_id,
        )


def test_query_schema_with_invalid_user_database_id() -> None:
    with pytest.raises(ValidationError):
        nl_query = "What is the total sales for the month of January?"
        sql_query = "SELECT SUM(sales) FROM sales WHERE month = 'January'"
        user_database_id = "1"
        QuerySchema(
            nl_query=nl_query,
            sql_query=sql_query,
            user_database_id=user_database_id,
        )


def test_query_schema_with_invalid_id() -> None:
    with pytest.raises(ValidationError):
        nl_query = "What is the total sales for the month of January?"
        sql_query = "SELECT SUM(sales) FROM sales WHERE month = 'January'"
        user_database_id = uuid4()
        id = "1"
        QuerySchema(
            nl_query=nl_query,
            sql_query=sql_query,
            user_database_id=user_database_id,
            id=id,
        )


def test_query_schema_with_missing_nl_query() -> None:
    with pytest.raises(ValidationError):
        sql_query = "SELECT SUM(sales) FROM sales WHERE month = 'January'"
        user_database_id = uuid4()
        QuerySchema(
            sql_query=sql_query,
            user_database_id=user_database_id,
        )


def test_query_schema_with_missing_user_database_id() -> None:
    with pytest.raises(ValidationError):
        nl_query = "What is the total sales for the month of January?"
        sql_query = "SELECT SUM(sales) FROM sales WHERE month = 'January'"
        QuerySchema(
            nl_query=nl_query,
            sql_query=sql_query,
        )


def test_query_schema_with_missing_sql_query() -> None:
    nl_query = "What is the total sales for the month of January?"
    user_database_id = uuid4()
    query = QuerySchema(
        nl_query=nl_query, user_database_id=user_database_id
    )
    assert query.nl_query == nl_query
    assert query.sql_query is None
    assert query.user_database_id == user_database_id
    assert query.id is None


def test_query_schema_with_missing_id() -> None:
    nl_query = "What is the total sales for the month of January?"
    sql_query = "SELECT SUM(sales) FROM sales WHERE month = 'January'"
    user_database_id = uuid4()
    query = QuerySchema(
        nl_query=nl_query, sql_query=sql_query, user_database_id=user_database_id
    )
    assert query.nl_query == nl_query
    assert query.sql_query == sql_query
    assert query.user_database_id == user_database_id
    assert query.id is None
