from app.models.UserLogin import UserLogin
class UserRepository:
    def __init__(self):
        pass


    @staticmethod
    def get_user_by_username(username):
        return UserLogin()