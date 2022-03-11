from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(50))
    hashed_password = Column(String)
    balance = Column(Integer)
    reg_date = Column(DateTime)
    operations = relationship('MoneyOperation', back_populates='user', cascade='all, delete')


class MoneyOperation(Base):
    __tablename__ = 'moneyoperation'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('User', back_populates='operations')
    value = Column(Integer)
