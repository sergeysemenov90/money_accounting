from tests.factories import MoneyOperationFactory, UserFactory, CategoryFactory
from tests.fixtures import new_user, category
from business.business_logic import change_user_balance, set_starting_balance


def test_create_user():
    user = UserFactory(balance=50000, email='myemail@email.com')
    assert user.balance == 50000
    assert user.email == 'myemail@email.com'


def test_create_category():
    category = CategoryFactory()
    assert category.name == 'Без категории'


def test_create_operation(new_user, category):
    operation = MoneyOperationFactory(user=new_user, category=category, value=3000)
    assert operation.user == new_user
    assert operation.value == 3000
    assert operation.category.id == 1


def test_spending_money_reduces_balance(new_user):
    operation = MoneyOperationFactory(user=new_user, value=-1000)
    change_user_balance(operation)
    assert new_user.balance == 99000


def test_adding_money_increases_balance(new_user):
    operation = MoneyOperationFactory(user=new_user, value=1000)
    change_user_balance(operation)
    assert new_user.balance == 101000


def test_set_starting_money_to_user():
    user = UserFactory(balance=None)
    set_starting_balance(user, 100000)
    assert user.balance == 100000


def test_add_operations_to_user(new_user):
    operation_1 = MoneyOperationFactory(user=new_user, value=5000)
    operation_2 = MoneyOperationFactory(user=new_user, value=3000)
    assert operation_1 in new_user.operations and operation_2 in new_user.operations
    change_user_balance(operation_1)
    change_user_balance(operation_2)
    assert new_user.balance == 108000
