from database import Base
from sqlalchemy import  Column, Integer, String, ForeignKey
from sqlalchemy.sql.sqltypes import  Date, Double
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    role = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    email = Column(String, nullable=False, unique= True)
    password = Column(String, nullable=False)


class Teacher(Base):
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True)
    bio = Column(String, nullable=True)
    subject = Column(String, nullable=False)
    currentInstitution = Column(String, nullable=False)
    offlineFee = Column(Integer, nullable=False)
    onlineFee = Column(Integer, nullable=False)
    userId = Column(Integer, ForeignKey('users.id'))
    user = relationship("User")
    rating = Column(Double, nullable=True, default= 0.0)
    balance = Column(Integer, nullable=True, default= 0)