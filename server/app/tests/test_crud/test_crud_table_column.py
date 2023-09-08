import uuid
from sqlalchemy.orm import Session
from app.crud.crud_table_column import CRUDTableColumn
from app.schemas.table_column import TableColumn as TableColumnSchema
from app.models.table_column import TableColumn as TableColumnModel


def test_create_table_column(db: Session) -> None:
    crud_table_column = CRUDTableColumn()
    table_column_obj = TableColumnSchema(
        name="test_column", data_type="int", database_table_id=uuid.uuid4()
    )
    result = crud_table_column.create(db=db, table_column_obj=table_column_obj)
    assert result.name == table_column_obj.name
    assert result.data_type == table_column_obj.data_type
    assert result.database_table_id == table_column_obj.database_table_id
    assert (
        db.query(TableColumnModel).filter(TableColumnModel.id == result.id).first()
        is not None
    )


def test_get_by_database_table_id(db: Session) -> None:
    crud_table_column = CRUDTableColumn()
    table_column_obj = TableColumnSchema(
        name="test_column", data_type="int", database_table_id=uuid.uuid4()
    )
    crud_table_column.create(db=db, table_column_obj=table_column_obj)
    result = crud_table_column.get_by_database_table_id(
        db=db, database_table_id=table_column_obj.database_table_id
    )
    assert result.count() == 1
    assert result[0].name == table_column_obj.name
    assert result[0].data_type == table_column_obj.data_type
    assert result[0].database_table_id == table_column_obj.database_table_id
    assert (
        db.query(TableColumnModel).filter(TableColumnModel.id == result[0].id).first()
        is not None
    )


def test_get_by_database_table_id_not_found(db: Session) -> None:
    crud_table_column = CRUDTableColumn()
    table_column_obj = TableColumnSchema(
        name="test_column", data_type="int", database_table_id=uuid.uuid4()
    )
    crud_table_column.create(db=db, table_column_obj=table_column_obj)
    result = crud_table_column.get_by_database_table_id(
        db=db, database_table_id=uuid.uuid4()
    )
    assert result.count() == 0
