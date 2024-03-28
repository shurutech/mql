import uuid
import pytest
from sqlalchemy.orm import Session
from app.models.query import Query as QueryModel
from app.crud.crud_query import CRUDQuery
from app.schemas.query import Query as QuerySchema


def test_create_query_with_null_sql_query(db: Session) -> None:
    user_database_id = uuid.uuid4()
    query_obj = QuerySchema(
        nl_query="What is the total sales for the month of January?",
        user_database_id=user_database_id,
    )
    query = CRUDQuery().create(
        db=db, query_obj=query_obj
    )
    assert query.nl_query == "What is the total sales for the month of January?"
    assert query.user_database_id == user_database_id
    assert query.sql_query is None
    assert query.id is not None


def test_create_query_with_not_null_sql_query(db: Session) -> None:
    user_database_id = uuid.uuid4()
    query_obj = QuerySchema(
        nl_query="What is the total sales for the month of January?",
        user_database_id=user_database_id,
        sql_query="SELECT SUM(sales) FROM sales WHERE month = 'January'",
    )
    query = CRUDQuery().create(
        db=db, query_obj=query_obj
    )
    assert query.nl_query == "What is the total sales for the month of January?"
    assert query.user_database_id == user_database_id
    assert (
        query.sql_query
        == "SELECT SUM(sales) FROM sales WHERE month = 'January'"
    )
    assert query.id is not None


def test_get_query(db: Session) -> None:
    user_database_id = uuid.uuid4()
    query_obj = QuerySchema(
        nl_query="What is the total sales for the month of January?",
        user_database_id=user_database_id,
        sql_query="SELECT SUM(sales) FROM sales WHERE month = 'January'",
    )
    query = CRUDQuery().create(
        db=db, query_obj=query_obj
    )
    query_from_db = CRUDQuery().get_by_id(db=db, id=query.id)
    assert (
        query_from_db.nl_query
        == "What is the total sales for the month of January?"
    )
    assert query_from_db.user_database_id == user_database_id
    assert (
        query_from_db.sql_query
        == "SELECT SUM(sales) FROM sales WHERE month = 'January'"
    )
    assert query_from_db.id == query.id
    assert (
        db.query(QueryModel)
        .filter(QueryModel.id == query_from_db.id)
        .first()
        is not None
    )


def test_get_query_by_database_id(db: Session) -> None:
    user_database_id = uuid.uuid4()
    query_obj_1 = QuerySchema(
        nl_query="What is the total sales for the month of January?",
        user_database_id=user_database_id,
        sql_query="SELECT SUM(sales) FROM sales WHERE month = 'January'",
    )
    query_obj_2 = QuerySchema(
        nl_query="What is the total sales for the month of Feburary?",
        user_database_id=user_database_id,
        sql_query="SELECT SUM(sales) FROM sales WHERE month = 'Feburary'",
    )
    query_1 = CRUDQuery().create(
        db=db, query_obj=query_obj_1
    )
    CRUDQuery().create(db=db, query_obj=query_obj_2)
    query_from_db = CRUDQuery().get_by_database_id(
        db=db, user_database_id=user_database_id
    )
    assert (
        query_from_db[0].nl_query
        == "What is the total sales for the month of January?"
    )
    assert query_from_db[0].user_database_id == user_database_id
    assert (
        query_from_db[0].sql_query
        == "SELECT SUM(sales) FROM sales WHERE month = 'January'"
    )
    assert query_from_db[0].id == query_1.id
    assert (
        db.query(QueryModel)
        .filter(
            QueryModel.user_database_id
            == query_from_db[0].user_database_id
        )
        .all()
        is not None
    )
    assert query_from_db.count() == 2


def test_get_query_by_database_id_where_sql_query_not_null(db: Session) -> None:
    user_database_id = uuid.uuid4()
    query_obj_1 = QuerySchema(
        nl_query="What is the total sales for the month of January?",
        user_database_id=user_database_id,
        sql_query="SELECT SUM(sales) FROM sales WHERE month = 'January'",
    )
    query_obj_2 = QuerySchema(
        nl_query="What is the total sales for the month of Feburary?",
        user_database_id=user_database_id,
    )
    query_1 = CRUDQuery().create(
        db=db, query_obj=query_obj_1
    )
    CRUDQuery().create(db=db, query_obj=query_obj_2)
    query_from_db = (
        CRUDQuery().get_by_datatbase_id_where_sql_query_not_null(
            db=db, user_database_id=user_database_id
        )
    )
    assert (
        query_from_db[0].nl_query
        == "What is the total sales for the month of January?"
    )
    assert query_from_db[0].user_database_id == user_database_id
    assert (
        query_from_db[0].sql_query
        == "SELECT SUM(sales) FROM sales WHERE month = 'January'"
    )
    assert query_from_db[0].id == query_1.id
    assert (
        db.query(QueryModel)
        .filter(
            QueryModel.user_database_id
            == query_from_db[0].user_database_id
        )
        .all()
        is not None
    )
    assert query_from_db.count() == 1


def test_insert_sql_query_by_id(db: Session) -> None:
    user_database_id = uuid.uuid4()
    query_obj = QuerySchema(
        nl_query="What is the total sales for the month of January?",
        user_database_id=user_database_id,
    )
    query = CRUDQuery().create(
        db=db, query_obj=query_obj
    )
    assert query.sql_query is None
    query_from_db = CRUDQuery().insert_sql_query_by_id(
        db=db,
        id=query.id,
        sql_query="SELECT SUM(sales) FROM sales WHERE month = 'January'",
    )
    assert (
        query_from_db.nl_query
        == "What is the total sales for the month of January?"
    )
    assert query_from_db.user_database_id == user_database_id
    assert (
        query_from_db.sql_query
        == "SELECT SUM(sales) FROM sales WHERE month = 'January'"
    )
    assert query_from_db.id == query.id
    assert (
        db.query(QueryModel)
        .filter(QueryModel.id == query_from_db.id)
        .first()
        is not None
    )


def test_insert_sql_query_by_id_with_null_sql_query(db: Session) -> None:
    user_database_id = uuid.uuid4()
    query_obj = QuerySchema(
        nl_query="What is the total sales for the month of January?",
        user_database_id=user_database_id,
        sql_query="SELECT SUM(sales) FROM sales WHERE month = 'January'",
    )
    query = CRUDQuery().create(
        db=db, query_obj=query_obj
    )
    assert (
        query.sql_query
        == "SELECT SUM(sales) FROM sales WHERE month = 'January'"
    )
    with pytest.raises(ValueError) as e:
        CRUDQuery().insert_sql_query_by_id(
            db=db, id=query.id, sql_query=None
        )
    assert str(e.value) == "SQL query already exists"


def test_insert_sql_query_by_id_with_not_null_sql_query(db: Session) -> None:
    user_database_id = uuid.uuid4()
    query_obj = QuerySchema(
        nl_query="What is the total sales for the month of January?",
        user_database_id=user_database_id,
        sql_query="SELECT SUM(sales) FROM sales WHERE month = 'January'",
    )
    query = CRUDQuery().create(
        db=db, query_obj=query_obj
    )
    assert (
        query.sql_query
        == "SELECT SUM(sales) FROM sales WHERE month = 'January'"
    )
    with pytest.raises(ValueError) as e:
        CRUDQuery().insert_sql_query_by_id(
            db=db,
            id=query.id,
            sql_query="SELECT SUM(sales) FROM sales WHERE month = 'Feburary'",
        )
    assert str(e.value) == "SQL query already exists"
