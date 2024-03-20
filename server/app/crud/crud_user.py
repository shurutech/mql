from typing import Optional
from uuid import UUID
from sqlalchemy.orm import Session
from bcrypt import checkpw

from app.models.user import User as UserModel


class CRUDUser:
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
