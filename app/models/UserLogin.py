

class UserLogin:
    def __init__(self, dictionary: object = {}):
        self.id = dictionary.get('id', '')
        self.name = dictionary.get('name', '')
        self.last_name = dictionary.get('last_name', '')
        self.password = dictionary.get('password', '')
        self.is_admin = dictionary.get('is_admin', False)
        self.username = dictionary.get('username', '')


    @classmethod
    def from_dict(cls, user):
        return cls(user)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "last_name": self.last_name,
            "password": self.password,
            "is_admin": self.is_admin,
            "username": self.username,
        }
