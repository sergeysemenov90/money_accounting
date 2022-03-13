import json
from abc import ABC

from fastapi.encoders import jsonable_encoder
from sqlalchemy.future import select
from sqlalchemy.orm import Session
from database.models import User, MoneyOperation, Category
from database.core import engine


class BaseRepository:
    """Родительский класс для наследования"""

    def __init__(self):
        self.session = Session(engine, future=True)

    def get(self, id):
        raise NotImplementedError

    def add(self, data):
        raise NotImplementedError

    def remove(self, id):
        raise NotImplementedError

    def update(self, data):
        raise NotImplementedError

    def list(self):
        raise NotImplementedError


class UserRepository(BaseRepository):

    def get(self, id):
        return self.session.query(User).filter_by(id=id).one()

    def add(self, data):
        user = User(**data)
        with self.session as session, session.begin():
            session.add(user)

    def remove(self, id):
        pass

    def update(self, data):
        pass

    def list(self):
        with self.session as session:
            result = session.query(User).all()
        return result


class MoneyOperationRepository(BaseRepository, ABC):

    def add(self, data):
        operation = MoneyOperation(**data)

        with self.session as session, session.begin():
            session.add(operation)


class CategoryRepository(BaseRepository, ABC):

    def add(self, data):
        category = Category(**data)

        with self.session as session, session.begin():
            session.add(category)
