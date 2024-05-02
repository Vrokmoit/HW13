from sqlalchemy import Column, Integer, ForeignKey, String, Date, Boolean, MetaData
from pydantic import BaseModel, EmailStr
from contactpr.database import Base
from sqlalchemy.orm import relationship
from passlib.context import CryptContext
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import MetaData

Base = declarative_base()

metadata = MetaData()

Base.metadata = metadata


class Contact(Base):
    __tablename__ = 'contacts'
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    phone_number = Column(String, index=True)
    birthday = Column(Date)
    additional_data = Column(String, nullable=True)
    owner_id = Column(Integer, ForeignKey('users.id'))
    owner = relationship("User", back_populates="contacts")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    contacts = relationship("Contact", back_populates="owner")
    avatar_url = Column(String)
    confirmed = Column(Boolean, default=False)

