import uuid
from app.models.database_table import DatabaseTable
from sqlalchemy.orm import Session
from app.crud.crud_database_table import CRUDDatabaseTable
from app.schemas.database_table import DatabaseTable as DatabaseTableSchema


def test_create_database_table_with_null_text_node(db: Session) -> None:
    crud_database_table = CRUDDatabaseTable()
    database_table_obj = DatabaseTableSchema(
        name="test_table", user_database_id=uuid.uuid4()
    )

    result = crud_database_table.create(db=db, database_table_obj=database_table_obj)

    assert result.name == database_table_obj.name
    assert result.user_database_id == database_table_obj.user_database_id
    assert result.text_node is None
    assert (
        db.query(DatabaseTable).filter(DatabaseTable.id == result.id).first()
        is not None
    )


def test_create_database_table_with_not_null_text_node(db: Session) -> None:
    crud_database_table = CRUDDatabaseTable()
    database_table_obj = DatabaseTableSchema(
        name="test_table", text_node="text_node", user_database_id=uuid.uuid4()
    )

    result = crud_database_table.create(db=db, database_table_obj=database_table_obj)

    assert result.name == database_table_obj.name
    assert result.text_node == database_table_obj.text_node
    assert result.user_database_id == database_table_obj.user_database_id
    assert (
        db.query(DatabaseTable).filter(DatabaseTable.id == result.id).first()
        is not None
    )


def test_get_by_user_database_id(db: Session) -> None:
    crud_database_table = CRUDDatabaseTable()
    database_table_obj = DatabaseTableSchema(
        name="test_table", text_node="text_node", user_database_id=uuid.uuid4()
    )
    crud_database_table.create(db=db, database_table_obj=database_table_obj)

    result = crud_database_table.get_by_user_database_id(
        db=db, user_database_id=database_table_obj.user_database_id
    )

    assert result.count() == 1
    assert result[0].name == database_table_obj.name
    assert result[0].text_node == database_table_obj.text_node
    assert result[0].user_database_id == database_table_obj.user_database_id
    assert (
        db.query(DatabaseTable).filter(DatabaseTable.id == result[0].id).first()
        is not None
    )


def test_get_by_user_database_id_not_found(db: Session) -> None:
    crud_database_table = CRUDDatabaseTable()
    database_table_obj = DatabaseTableSchema(
        name="test_table", text_node="text_node", user_database_id=uuid.uuid4()
    )
    crud_database_table.create(db=db, database_table_obj=database_table_obj)

    result = crud_database_table.get_by_user_database_id(
        db=db, user_database_id=uuid.uuid4()
    )

    assert result.count() == 0


def test_get_by_id(db: Session) -> None:
    crud_database_table = CRUDDatabaseTable()
    database_table_obj = DatabaseTableSchema(
        name="test_table", text_node="text_node", user_database_id=uuid.uuid4()
    )
    database_table = crud_database_table.create(
        db=db, database_table_obj=database_table_obj
    )

    result = crud_database_table.get_by_id(db=db, id=database_table.id)

    assert result is not None
    assert result.name == database_table_obj.name
    assert result.text_node == database_table_obj.text_node
    assert result.user_database_id == database_table_obj.user_database_id
    assert result.id == database_table.id
    assert (
        db.query(DatabaseTable).filter(DatabaseTable.id == result.id).first()
        is not None
    )


def test_get_by_ids(db: Session) -> None:
    crud_database_table = CRUDDatabaseTable()
    tables = []
    for index in range(5):
        database_table_obj = DatabaseTableSchema(
            name=f"test_table_{index}",
            text_node=f"text_node_{index}",
            user_database_id=uuid.uuid4(),
        )
        table = crud_database_table.create(db=db, database_table_obj=database_table_obj)
        tables.append(table)

    result = crud_database_table.get_by_ids(db, [table.id for table in tables])

    assert result.count() == 5
    for index in range(5):
        assert result[index].name == f"test_table_{index}"
        assert result[index].text_node == f"text_node_{index}"
        assert result[index].user_database_id == tables[index].user_database_id
        assert (
            db.query(DatabaseTable).filter(DatabaseTable.id == result[index].id).first()
            is not None
        )


def test_upsert_text_node_by_id_when_inserting_text_node_first_time(
    db: Session,
) -> None:
    crud_database_table = CRUDDatabaseTable()
    database_table_obj = DatabaseTableSchema(
        name="test_table", user_database_id=uuid.uuid4()
    )
    database_table = crud_database_table.create(
        db=db, database_table_obj=database_table_obj
    )

    assert database_table.text_node is None

    crud_database_table.upsert_text_node_by_id(
        db=db, table_id=database_table.id, text_node="text_node"
    )

    result = crud_database_table.get_by_id(db=db, id=database_table.id)

    assert result is not None
    assert result.name == database_table_obj.name
    assert result.text_node == "text_node"
    assert result.user_database_id == database_table_obj.user_database_id
    assert (
        db.query(DatabaseTable).filter(DatabaseTable.id == result.id).first()
        is not None
    )


def test_upsert_text_node_by_id_when_updating_text_node(db: Session) -> None:
    crud_database_table = CRUDDatabaseTable()
    database_table_obj = DatabaseTableSchema(
        name="test_table", text_node="text_node", user_database_id=uuid.uuid4()
    )
    database_table = crud_database_table.create(
        db=db, database_table_obj=database_table_obj
    )

    assert database_table.text_node == "text_node"

    crud_database_table.upsert_text_node_by_id(
        db=db, table_id=database_table.id, text_node="updated_text_node"
    )

    result = crud_database_table.get_by_id(db=db, id=database_table.id)

    assert result is not None
    assert result.name == database_table_obj.name
    assert result.text_node == "updated_text_node"
    assert result.user_database_id == database_table_obj.user_database_id
    assert (
        db.query(DatabaseTable).filter(DatabaseTable.id == result.id).first()
        is not None
    )

def test_delete_table_by_user_database_id(db: Session) -> None:
    crud_database_table = CRUDDatabaseTable()
    user_database_id = uuid.uuid4()
    for index in range(5):
        database_table_obj = DatabaseTableSchema(
            name=f"test_table_{index}",
            text_node=f"text_node_{index}",
            user_database_id=user_database_id,
        )
        crud_database_table.create(db=db, database_table_obj=database_table_obj)

    crud_database_table.delete_by_user_database_id(db=db, user_database_id=user_database_id)

    result = crud_database_table.get_by_user_database_id(db=db, user_database_id=user_database_id)

    assert result.count() == 0
    assert db.query(DatabaseTable).filter(DatabaseTable.user_database_id == user_database_id).count() == 0