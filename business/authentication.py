def get_user_by_email(repository, email):
    user = repository.get(email)
    return user
