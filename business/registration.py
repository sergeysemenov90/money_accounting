from typing import Optional

from database.models import User
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def check_and_update_register_data(reg_data) -> Optional[dict]:
    password = reg_data.get('password') if reg_data.get('password') == reg_data.get('password_again') else None
    email = reg_data.get('email')

    hashed_password = password_hasher(password)

    if all((email, hashed_password)):
        confirm_data = {'email': email, 'hashed_password': hashed_password}
        return confirm_data


def password_hasher(password: str) -> str:
    if password:
        return pwd_context.hash(password)

