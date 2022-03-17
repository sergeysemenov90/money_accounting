from tests.fixtures import new_user, another_user
from business.authentication import get_user_by_email
from repositories.fake_repositories import FakeUserRepository


def test_get_user_by_email(new_user, another_user):
    repository = FakeUserRepository(users=[new_user, another_user])
    email = new_user.email
    user = get_user_by_email(repository, email)
    assert user == new_user


def test_authenticate_user():
