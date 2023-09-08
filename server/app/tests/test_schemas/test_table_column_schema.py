import pytest
from pydantic import ValidationError
from uuid import uuid4
from app.schemas.table_column import TableColumn


def test_table_column_schema_with_valid_data() -> None:
    name = "Test Column"
    data_type = "Character Varying"
    database_table_id = uuid4()

    table_column = TableColumn(
        name=name, data_type=data_type, database_table_id=database_table_id
    )

    assert table_column.name == name
    assert table_column.data_type == data_type
    assert table_column.database_table_id == database_table_id


def test_table_column_schema_with_missing_name() -> None:
    data_type = "Character Varying"
    database_table_id = uuid4()

    with pytest.raises(ValidationError):
        TableColumn(name=None, data_type=data_type, database_table_id=database_table_id)


def test_table_column_schema_with_invalid_name() -> None:
    name = 123
    data_type = "Character Varying"
    database_table_id = uuid4()

    with pytest.raises(ValidationError):
        TableColumn(name=name, data_type=data_type, database_table_id=database_table_id)


def test_table_column_schema_with_missing_data_type() -> None:
    name = "Test Column"
    database_table_id = uuid4()

    with pytest.raises(ValidationError):
        TableColumn(name=name, data_type=None, database_table_id=database_table_id)


def test_table_column_schema_with_invalid_data_type() -> None:
    name = "Test Column"
    data_type = 123
    database_table_id = uuid4()

    with pytest.raises(ValidationError):
        TableColumn(name=name, data_type=data_type, database_table_id=database_table_id)


def test_table_column_schema_with_missing_database_table_id() -> None:
    name = "Test Column"
    data_type = "Character Varying"

    with pytest.raises(ValidationError):
        TableColumn(name=name, data_type=data_type, database_table_id=None)


def test_table_column_schema_with_invalid_database_table_id() -> None:
    name = "Test Column"
    data_type = "Character Varying"
    database_table_id = "invalid_uuid"

    with pytest.raises(ValidationError):
        TableColumn(name=name, data_type=data_type, database_table_id=database_table_id)
