from tests.factories import UserFactory
from business.registration import register_user, password_hasher


def test_user_password_was_hashed():
    password_to_hash = 'abc' * 3
    hashed_password = password_hasher(password_to_hash)
    assert hashed_password == 'fakehashed' + password_to_hash


def test_user_can_register_with_correct_data():
    reg_data = {'email': 'test@test.ru',
                'password': 'abc' * 3,
                'password_again': 'abc' * 3}
    user = register_user(reg_data)

    assert user.email == 'test@test.ru'
    assert user.hashed_password is not None
    assert user.hashed_password != 'abc * 3'


def test_user_cant_register_with_incorrect_password():
    reg_data = {'email': 'test@test.ru',
                'password': 'abc' * 3,
                'password_again': 'abc' * 4}

    user = register_user(reg_data)
    assert user is None


def test_user_cant_register_with_empty_email():
    reg_data = {'email': '',
                'password': 'abc' * 3,
                'password_again': 'abc' * 3}
    user = register_user(reg_data)
    assert user is None

