from sqlalchemy.orm import Session
from app.models.user import User as UserModel


def test_as_dict_method(valid_user_model: UserModel) -> None:
    result = valid_user_model.as_dict()

    assert "id" in result
    assert isinstance(result["id"], str)
    assert result == {
        "name": valid_user_model.name,
        "email": valid_user_model.email,
        "id": result["id"],
        "created_at": result["created_at"],
        "updated_at": result["updated_at"],
        "hashed_key": valid_user_model.hashed_key,
    }


def test_timestamp_on_create(valid_user_model: UserModel) -> None:
    assert valid_user_model.created_at is not None
    assert valid_user_model.updated_at is not None
    assert valid_user_model.created_at == valid_user_model.updated_at


def test_timestamp_on_update(valid_user_model: UserModel, db: Session) -> None:
    valid_user_model.name = "test_user_updated"
    db.commit()
    assert valid_user_model.created_at is not None
    assert valid_user_model.updated_at is not None
    assert valid_user_model.created_at != valid_user_model.updated_at
