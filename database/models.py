from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean
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

    def __str__(self):
        return f'{self.email}'


class MoneyOperation(Base):
    __tablename__ = 'moneyoperation'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    category_id = Column(Integer, ForeignKey('category.id'), default=1)
    user = relationship('User', back_populates='operations')
    category = relationship('Category', back_populates='operations')
    value = Column(Integer)


class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30))
    operations = relationship('MoneyOperation', back_populates='category')
