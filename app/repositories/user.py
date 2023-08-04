from models.UserLogin import UserLogin
from db.connection import getConnection
from models.User import User
import uuid
from models.User import User


class UserRepository:

    @staticmethod
    def get_all():
        users = list(getConnection().UserLogin.find())
        return [ UserLogin.from_dict(user) for user in users ]

    @staticmethod
    def get_user_by_username(username):
        user = getConnection().UserLogin.find_one({'username': username})
        if user is None:
            return None
        return UserLogin.from_dict(user)

    @classmethod
    def save_new_user_login(cls, user):
        user.id = str(uuid.uuid4())
        cls.save_new_user(User(id=user.id))
        # getConnection().User.insert_one(User(id=user.id).to_dict())
        getConnection().UserLogin.insert_one(user.to_dict())

    @staticmethod
    def find_by_id(user_id) -> User:
        userdb = getConnection().User.find_one({'id': user_id})
        if userdb is None:
            return User()
        else:
            return User.from_dict(userdb)

    @staticmethod
    def save_new_user(user):
        return getConnection().User.insert_one(user.to_dict())

    @staticmethod
    def update_user(user):
        return getConnection().User.update_one({'id': user.id}, {"$set": { 'history': user.history }})

    @staticmethod
    def delete(user):
        return getConnection().UserLogin.delete_one({'id': user.id})