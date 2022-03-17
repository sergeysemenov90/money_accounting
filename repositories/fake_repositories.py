class FakeUserRepository:
    def __init__(self, users):
        self.users = list(users)

    def get(self, email):
        return next(user for user in self.users if user.email == email)

    def add(self, user):
        self.users.append(user)

    def remove(self, id):
        user = self.get(id)
        self.users.remove(user)

    def update(self, user):
        user_to_update = self.get(user.id)
        self.users.remove(user_to_update)
        self.users.append(user)

    def list(self):
        return {'users': self.users}
