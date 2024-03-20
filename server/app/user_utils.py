# app/user_utils.py
from  app.crud.crud_user import crud_user
from  app.schemas.user import User
from  app.db.session import sessionLocal
import logging

def create_default_user():
    db = sessionLocal()
    try:
        name = "Admin"
        default_email = "admin@example.com"
        user = crud_user.get_by_email(db, default_email)
        if user is None:
            password =  "admin"
            crud_user.create(db, User(name=name, email=default_email, password=password))
            logging.info("Default user created.")
        else:
            logging.info("Default user already exists.")
    except Exception as e:
        logging.error(f"Failed to initialize database: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    create_default_user()