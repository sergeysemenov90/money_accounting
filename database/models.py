from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class MoneyOperation(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    user = Column(ForeignKey)


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(50))
    hashed_password = Column(String)
    balance = Column(Integer)
    reg_date = Column(DateTime)


class Goal(Base):
    pass
