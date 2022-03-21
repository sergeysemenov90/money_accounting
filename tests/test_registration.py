from tests.factories import UserFactory
from business.registration import check_and_update_register_data, password_hasher, hash_scheme


def test_user_can_register_with_correct_data():
    reg_data = {'email': 'test@test.ru',
                'password': 'abc' * 3,
                'password_again': 'abc' * 3}
    confirm_data = check_and_update_register_data(reg_data)

    assert confirm_data['email'] == 'test@test.ru'
    assert confirm_data['hashed_password'] is not None
    assert confirm_data['hashed_password'] != 'abc * 3'


def test_user_has_hashed_password():
    reg_data = {'email': 'test@test.ru',
                'password': 'abc' * 3,
                'password_again': 'abc' * 3}
    password = reg_data['password']
    confirm_data = check_and_update_register_data(reg_data)
    user = UserFactory(**confirm_data)

    assert hash_scheme.verify(password, user.hashed_password)


def test_user_cant_register_with_incorrect_password():
    reg_data = {'email': 'test@test.ru',
                'password': 'abc' * 3,
                'password_again': 'abc' * 4}

    confirm_data = check_and_update_register_data(reg_data)
    assert confirm_data is None


def test_user_cant_register_with_empty_email():
    reg_data = {'email': '',
                'password': 'abc' * 3,
                'password_again': 'abc' * 3}
    confirm_data = check_and_update_register_data(reg_data)
    assert confirm_data is None

