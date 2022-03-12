import factory
from factory.fuzzy import FuzzyText

from database.models import User


class UserFactory(factory.Factory):
    class Meta:
        model = User

