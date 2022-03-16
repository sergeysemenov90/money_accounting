def change_user_balance(operation):
    user = operation.user
    user.balance += operation.value
    return user.balance


def set_starting_balance(user, value):
    user.balance = value
