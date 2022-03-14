import factory

from database.models import User, MoneyOperation


class UserFactory(factory.Factory):
    id = 1
    email = 'test@test.ru'
    balance = 100000

    class Meta:
        model = User


class MoneyOperationFactory(factory.Factory):
    id = 1

    class Meta:
        model = MoneyOperation
