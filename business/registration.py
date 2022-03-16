from typing import Optional

from database.models import User


def register_user(reg_data) -> Optional[User]:
    password = reg_data.get('password') if reg_data.get('password') == reg_data.get('password_again') else None
    email = reg_data.get('email')

    if password:
        hashed_password = password_hasher(password)
    else:
        return None

    if all((email, hashed_password)):
        user = User(email=email, hashed_password=hashed_password)
        return user


def password_hasher(password: str) -> str:
    return 'fakehashed' + password

