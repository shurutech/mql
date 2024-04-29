from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os
from uuid import UUID
import getpass
from bcrypt import hashpw, gensalt
import uuid
from sqlalchemy import String, UUID
from sqlalchemy.orm import mapped_column
from sqlalchemy import Column, DateTime, func
from sqlalchemy.orm import DeclarativeBase
import logging

def hash_password(password: str) -> str:
    hashed_password = hashpw(password.encode("utf-8"), gensalt())
    return hashed_password.decode("utf-8")

class Base(DeclarativeBase):
    pass


class TimestampBase(Base):
    __abstract__ = True
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())


class User(TimestampBase):
    __tablename__ = "users"

    id = mapped_column(
        UUID, primary_key=True, unique=True, index=True, default=uuid.uuid4
    )
    name = mapped_column(String, nullable=False)
    email = mapped_column(String, unique=True, nullable=False)
    hashed_password = mapped_column(String, nullable=False)

    def as_dict(self) -> dict:
        return {
            "name": self.name,
            "email": self.email,
            "id": str(self.id),
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }


load_dotenv()

engine = create_engine(os.getenv("DATABASE_URL"), echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


email = input("Enter your email: ")
password = getpass.getpass("Enter your password: ")
name = input("Enter your name: ")

user = SessionLocal().query(User).filter(User.email == email).first()

if  user:
    logging.getLogger("mql").info("User already exists with email {}".format(email))
    exit()

with SessionLocal() as session:
    user = User(email=email, hashed_password= hash_password(password=password), name=name)
    
    session.add(user)
    session.commit()  
    session.refresh(user) 
    session.close() 


print("User created successfully!!")
