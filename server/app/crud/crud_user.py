from typing import Optional
from uuid import UUID
from sqlalchemy.orm import Session
from bcrypt import hashpw, gensalt, checkpw

from app.models.user import User as UserModel
from app.schemas.user import User


def hash_password(password: str) -> str:
    hashed_password = hashpw(password.encode("utf-8"), gensalt())
    return hashed_password.decode("utf-8")


class CRUDUser:
    def create(self, db: Session, user_obj: User) -> UserModel:
        user = UserModel(
            email=user_obj.email,
            hashed_password=hash_password(user_obj.password),
            name=user_obj.name,
        )
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

    def get_by_id(self, db: Session, id: UUID) -> Optional[UserModel]:
        return db.query(UserModel).filter(UserModel.id == id).first()

    def get_by_email(self, db: Session, email: str) -> Optional[UserModel]:
        return db.query(UserModel).filter(UserModel.email == email).first()

    def authenticate(
        self, db: Session, email: str, password: str
    ) -> Optional[UserModel]:
        user = self.get_by_email(db, email=email)
        if not user:
            return None
        if not checkpw(password.encode("utf-8"), user.hashed_password.encode("utf-8")):
            return None
        return user


crud_user = CRUDUser()
