import uuid
import pytest
from sqlalchemy.orm import Session
from app.models.query_history import QueryHistory as QueryHistoryModel
from app.crud.crud_query_history import CRUDQueryHistory
from app.schemas.query_history import QueryHistory as QueryHistorySchema


def test_create_query_history_with_null_sql_query(db: Session) -> None:
    user_database_id = uuid.uuid4()
    query_history_obj = QueryHistorySchema(
        nl_query="What is the total sales for the month of January?",
        user_database_id=user_database_id,
    )
    query_history = CRUDQueryHistory().create(
        db=db, query_history_obj=query_history_obj
    )
    assert query_history.nl_query == "What is the total sales for the month of January?"
    assert query_history.user_database_id == user_database_id
    assert query_history.sql_query is None
    assert query_history.id is not None


def test_create_query_history_with_not_null_sql_query(db: Session) -> None:
    user_database_id = uuid.uuid4()
    query_history_obj = QueryHistorySchema(
        nl_query="What is the total sales for the month of January?",
        user_database_id=user_database_id,
        sql_query="SELECT SUM(sales) FROM sales WHERE month = 'January'",
    )
    query_history = CRUDQueryHistory().create(
        db=db, query_history_obj=query_history_obj
    )
    assert query_history.nl_query == "What is the total sales for the month of January?"
    assert query_history.user_database_id == user_database_id
    assert (
        query_history.sql_query
        == "SELECT SUM(sales) FROM sales WHERE month = 'January'"
    )
    assert query_history.id is not None


def test_get_query_history_by_id(db: Session) -> None:
    user_database_id = uuid.uuid4()
    query_history_obj = QueryHistorySchema(
        nl_query="What is the total sales for the month of January?",
        user_database_id=user_database_id,
        sql_query="SELECT SUM(sales) FROM sales WHERE month = 'January'",
    )
    query_history = CRUDQueryHistory().create(
        db=db, query_history_obj=query_history_obj
    )
    query_history_from_db = CRUDQueryHistory().get_by_id(db=db, id=query_history.id)
    assert (
        query_history_from_db.nl_query
        == "What is the total sales for the month of January?"
    )
    assert query_history_from_db.user_database_id == user_database_id
    assert (
        query_history_from_db.sql_query
        == "SELECT SUM(sales) FROM sales WHERE month = 'January'"
    )
    assert query_history_from_db.id == query_history.id
    assert (
        db.query(QueryHistoryModel)
        .filter(QueryHistoryModel.id == query_history_from_db.id)
        .first()
        is not None
    )


def test_get_query_history_by_database_id(db: Session) -> None:
    user_database_id = uuid.uuid4()
    query_history_obj_1 = QueryHistorySchema(
        nl_query="What is the total sales for the month of January?",
        user_database_id=user_database_id,
        sql_query="SELECT SUM(sales) FROM sales WHERE month = 'January'",
    )
    query_history_obj_2 = QueryHistorySchema(
        nl_query="What is the total sales for the month of Feburary?",
        user_database_id=user_database_id,
        sql_query="SELECT SUM(sales) FROM sales WHERE month = 'Feburary'",
    )
    query_history_1 = CRUDQueryHistory().create(
        db=db, query_history_obj=query_history_obj_1
    )
    CRUDQueryHistory().create(db=db, query_history_obj=query_history_obj_2)
    query_history_from_db = CRUDQueryHistory().get_by_database_id(
        db=db, user_database_id=user_database_id
    )
    assert (
        query_history_from_db[0].nl_query
        == "What is the total sales for the month of January?"
    )
    assert query_history_from_db[0].user_database_id == user_database_id
    assert (
        query_history_from_db[0].sql_query
        == "SELECT SUM(sales) FROM sales WHERE month = 'January'"
    )
    assert query_history_from_db[0].id == query_history_1.id
    assert (
        db.query(QueryHistoryModel)
        .filter(
            QueryHistoryModel.user_database_id
            == query_history_from_db[0].user_database_id
        )
        .all()
        is not None
    )
    assert query_history_from_db.count() == 2


def test_get_query_history_by_database_id_where_sql_query_not_null(db: Session) -> None:
    user_database_id = uuid.uuid4()
    query_history_obj_1 = QueryHistorySchema(
        nl_query="What is the total sales for the month of January?",
        user_database_id=user_database_id,
        sql_query="SELECT SUM(sales) FROM sales WHERE month = 'January'",
    )
    query_history_obj_2 = QueryHistorySchema(
        nl_query="What is the total sales for the month of Feburary?",
        user_database_id=user_database_id,
    )
    query_history_1 = CRUDQueryHistory().create(
        db=db, query_history_obj=query_history_obj_1
    )
    CRUDQueryHistory().create(db=db, query_history_obj=query_history_obj_2)
    query_history_from_db = (
        CRUDQueryHistory().get_by_datatbase_id_where_sql_query_not_null(
            db=db, user_database_id=user_database_id
        )
    )
    assert (
        query_history_from_db[0].nl_query
        == "What is the total sales for the month of January?"
    )
    assert query_history_from_db[0].user_database_id == user_database_id
    assert (
        query_history_from_db[0].sql_query
        == "SELECT SUM(sales) FROM sales WHERE month = 'January'"
    )
    assert query_history_from_db[0].id == query_history_1.id
    assert (
        db.query(QueryHistoryModel)
        .filter(
            QueryHistoryModel.user_database_id
            == query_history_from_db[0].user_database_id
        )
        .all()
        is not None
    )
    assert query_history_from_db.count() == 1


def test_insert_sql_query_by_id(db: Session) -> None:
    user_database_id = uuid.uuid4()
    query_history_obj = QueryHistorySchema(
        nl_query="What is the total sales for the month of January?",
        user_database_id=user_database_id,
    )
    query_history = CRUDQueryHistory().create(
        db=db, query_history_obj=query_history_obj
    )
    assert query_history.sql_query is None
    query_history_from_db = CRUDQueryHistory().insert_sql_query_by_id(
        db=db,
        id=query_history.id,
        sql_query="SELECT SUM(sales) FROM sales WHERE month = 'January'",
    )
    assert (
        query_history_from_db.nl_query
        == "What is the total sales for the month of January?"
    )
    assert query_history_from_db.user_database_id == user_database_id
    assert (
        query_history_from_db.sql_query
        == "SELECT SUM(sales) FROM sales WHERE month = 'January'"
    )
    assert query_history_from_db.id == query_history.id
    assert (
        db.query(QueryHistoryModel)
        .filter(QueryHistoryModel.id == query_history_from_db.id)
        .first()
        is not None
    )


def test_insert_sql_query_by_id_with_null_sql_query(db: Session) -> None:
    user_database_id = uuid.uuid4()
    query_history_obj = QueryHistorySchema(
        nl_query="What is the total sales for the month of January?",
        user_database_id=user_database_id,
        sql_query="SELECT SUM(sales) FROM sales WHERE month = 'January'",
    )
    query_history = CRUDQueryHistory().create(
        db=db, query_history_obj=query_history_obj
    )
    assert (
        query_history.sql_query
        == "SELECT SUM(sales) FROM sales WHERE month = 'January'"
    )
    with pytest.raises(ValueError) as e:
        CRUDQueryHistory().insert_sql_query_by_id(
            db=db, id=query_history.id, sql_query=None
        )
    assert str(e.value) == "SQL query already exists"


def test_insert_sql_query_by_id_with_not_null_sql_query(db: Session) -> None:
    user_database_id = uuid.uuid4()
    query_history_obj = QueryHistorySchema(
        nl_query="What is the total sales for the month of January?",
        user_database_id=user_database_id,
        sql_query="SELECT SUM(sales) FROM sales WHERE month = 'January'",
    )
    query_history = CRUDQueryHistory().create(
        db=db, query_history_obj=query_history_obj
    )
    assert (
        query_history.sql_query
        == "SELECT SUM(sales) FROM sales WHERE month = 'January'"
    )
    with pytest.raises(ValueError) as e:
        CRUDQueryHistory().insert_sql_query_by_id(
            db=db,
            id=query_history.id,
            sql_query="SELECT SUM(sales) FROM sales WHERE month = 'Feburary'",
        )
    assert str(e.value) == "SQL query already exists"
