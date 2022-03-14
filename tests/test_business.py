from tests.factories import MoneyOperationFactory
from tests.fixtures import new_user
from database.service import change_user_balance


def test_spending_money_reduces_balance(new_user):
    operation = MoneyOperationFactory(user=new_user, value=-1000)
    change_user_balance(operation)
    assert new_user.balance == 99000


def test_adding_money_increases_balance(new_user):
    operation = MoneyOperationFactory(user=new_user, value=1000)
    change_user_balance(operation)
    assert new_user.balance == 101000
