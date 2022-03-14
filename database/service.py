import datetime


def get_user():
    user = {'id': 1,
            'email': 'test@test.ru',
            'hashed_password': 'somehashedpassword',
            'balance': 120000,
            'reg_date': datetime.datetime.now(),
            'operations': [-3000, 2500, 2800, -1800],
            }
    return user


def change_user_balance(operation):
    user = operation.user
    user.balance += operation.value
