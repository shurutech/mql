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
            connection_string=user_database_obj.connection_string,
        )
        db.add(user_database)
        db.flush()
        return user_database

    def get_by_user_id(self, db: Session, user_id: UUID) -> UserDatabaseModel:
        return db.query(UserDatabaseModel).filter(UserDatabaseModel.user_id == user_id)

    def get_by_id(self, db: Session, id: UUID) -> UserDatabaseModel:
        return db.query(UserDatabaseModel).filter(UserDatabaseModel.id == id).first()

    def delete_by_id(self, db: Session, id: UUID) -> None:
        db.query(UserDatabaseModel).filter(UserDatabaseModel.id == id).delete()

crud_user_database = CRUDUserDatabase()
