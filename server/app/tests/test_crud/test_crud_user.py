from sqlalchemy.orm import Session
from app.models.user import User as UserModel
from app.crud.crud_user import CRUDUser
from app.schemas.user import User as UserSchema


def test_get_by_email(db: Session, valid_user: UserSchema) -> None:
    crud_user = CRUDUser()
    crud_user.create(db=db, user_obj=valid_user)
    result = crud_user.get_by_email(db=db, email=valid_user.email)

    assert result is not None
    assert result.name == valid_user.name
    assert result.email == valid_user.email
    assert (
        db.query(UserModel).filter(UserModel.email == result.email).first() is not None
    )


def test_get_by_id(db: Session, valid_user_model: UserModel) -> None:
    crud_user = CRUDUser()
    result = crud_user.get_by_id(db=db, id=valid_user_model.id)

    assert result is not None
    assert result.name == valid_user_model.name
    assert result.email == valid_user_model.email
    assert (
        db.query(UserModel).filter(UserModel.email == result.email).first() is not None
    )
