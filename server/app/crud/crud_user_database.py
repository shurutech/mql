from uuid import UUID
from sqlalchemy.orm import Session
from app.models.user_database import UserDatabase as UserDatabaseModel
from app.schemas.user_database import UserDatabase as UserDatabaseSchema


class CRUDUserDatabase:
    def create(
        self, db: Session, user_database_obj: UserDatabaseSchema
    ) -> UserDatabaseModel:
        user_database = UserDatabaseModel(
            name=user_database_obj.name,
            user_id=user_database_obj.user_id,
        )
        db.add(user_database)
        db.commit()
        db.refresh(user_database)
        return user_database

    def get_by_user_id(self, db: Session, user_id: UUID) -> UserDatabaseModel:
        return db.query(UserDatabaseModel).filter(UserDatabaseModel.user_id == user_id)

    def get_by_id(self, db: Session, id: UUID) -> UserDatabaseModel:
        return db.query(UserDatabaseModel).filter(UserDatabaseModel.id == id).first()


crud_user_database = CRUDUserDatabase()
