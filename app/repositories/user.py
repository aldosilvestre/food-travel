from models.UserLogin import UserLogin
from db.connection import getConnection
from models.User import User
import uuid
from models.User import User


class UserRepository:

    @staticmethod
    def get_user_by_username(username):
        user = getConnection().UserLogin.find_one({'username': username})
        if user is None:
            return None
        return UserLogin.from_dict(user)

    @staticmethod
    def save_new_user(user):
        user.id = str(uuid.uuid4())
        getConnection().User.insert_one(User(id=user.id).to_dict())
        getConnection().UserLogin.insert_one(user.to_dict())

    @staticmethod
    def find_by_id(user_id) -> User:
        return User.from_dict(getConnection().User.find_one({'id': user_id}))