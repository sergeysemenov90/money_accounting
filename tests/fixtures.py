import pytest

from tests.factories import UserFactory, CategoryFactory


@pytest.fixture()
def new_user():
    return UserFactory()


@pytest.fixture()
def another_user():
    return UserFactory(id=2, email='test@test2.ru')


@pytest.fixture()
def category():
    return CategoryFactory()
