import pytest

from tests.factories import UserFactory, CategoryFactory
from repositories import fake_repositories


@pytest.fixture()
def new_user():
    return UserFactory()


@pytest.fixture()
def another_user():
    return UserFactory(id=2, email='test@test2.ru')


@pytest.fixture()
def category():
    return CategoryFactory()


@pytest.fixture()
def fake_user_repository_2(new_user, another_user):
    repository = fake_repositories.FakeUserRepository()
    return repository
