from sqlalchemy.orm import Session
from database.models import User


class UserRepository:
    def __init__(self, session: Session):
        self.session = session

    def get(self, id):
        return self.session.query(User).filter_by(id=id).one()

    def add(self):
        pass

    def remove(self):
        pass

    def update(self):
        pass

    def list(self):
        pass
