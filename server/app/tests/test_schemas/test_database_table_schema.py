import pytest
from pydantic import ValidationError
from uuid import uuid4
from app.schemas.database_table import DatabaseTable


def test_database_table_schema_with_valid_data() -> None:
    name = "Test Table"
    user_database_id = uuid4()

    database_table = DatabaseTable(name=name, user_database_id=user_database_id)

    assert database_table.name == name
    assert database_table.user_database_id == user_database_id


def test_database_table_schema_with_missing_name() -> None:
    user_database_id = uuid4()

    with pytest.raises(ValidationError):
        DatabaseTable(name=None, user_database_id=user_database_id)


def test_database_table_schema_with_invalid_name() -> None:
    name = 123
    user_database_id = uuid4()

    with pytest.raises(ValidationError):
        DatabaseTable(name=name, user_database_id=user_database_id)


def test_database_table_schema_with_missing_user_database_id() -> None:
    name = "Test Table"

    with pytest.raises(ValidationError):
        DatabaseTable(name=name, user_database_id=None)


def test_database_table_schema_with_invalid_user_database_id() -> None:
    name = "Test Table"
    user_database_id = "invalid_uuid"

    with pytest.raises(ValidationError):
        DatabaseTable(name=name, user_database_id=user_database_id)


def test_database_table_schema_with_missing_text_node() -> None:
    name = "Test Table"
    user_database_id = uuid4()

    database_table = DatabaseTable(name=name, user_database_id=user_database_id)

    assert database_table.name == name
    assert database_table.user_database_id == user_database_id
    assert database_table.text_node is None


def test_database_table_schema_with_invalid_text_node() -> None:
    name = "Test Table"
    user_database_id = uuid4()
    text_node = 123

    with pytest.raises(ValidationError):
        DatabaseTable(name=name, user_database_id=user_database_id, text_node=text_node)


def test_database_table_schema_with_valid_text_node() -> None:
    name = "Test Table"
    user_database_id = uuid4()
    text_node = "text_node"

    database_table = DatabaseTable(
        name=name, user_database_id=user_database_id, text_node=text_node
    )

    assert database_table.name == name
    assert database_table.user_database_id == user_database_id
    assert database_table.text_node == text_node
