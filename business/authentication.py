from passlib.context import CryptContext

hash_scheme = CryptContext(schemes=['bcrypt'], deprecated='auto')


def verify_user_password(password, hashed_password):
    return hash_scheme.verify(password, hashed_password)


def create_access_token(email, expire_delta):
    data = {
        'sub': email
    }
    data.update(expire_delta)
