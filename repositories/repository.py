from abc import ABC

from sqlalchemy import update
from sqlalchemy.orm import Session

from business.business_logic import change_user_balance
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
    """CRUD операции для модели User"""

    def get(self, id):
        return self.session.query(User).filter_by(id=id).one()

    def add(self, user):
        with self.session as session, session.begin():
            session.add(user)

    def remove(self, id):
        pass

    def update(self, user):
        with self.session as session, session.begin():
            session.execute()

    def list(self):
        with self.session as session:
            result = session.query(User).all()
        return result


class MoneyOperationRepository(BaseRepository, ABC):
    """CRUD операции для модели MoneyOperation"""

    def add(self, operation):
        user_balance = change_user_balance(operation)

        with self.session as session, session.begin():
            session.add(operation)
            session.execute(update(User).where(User.id == operation.user.id).values(balance=user_balance))


class CategoryRepository(BaseRepository, ABC):
    """CRUD операции для модели Category"""

    def add(self, category):
        with self.session as session, session.begin():
            session.add(category)
