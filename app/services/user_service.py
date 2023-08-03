from services.parametrics_service import parametric_service
from core.Session import Session
from models.UserLogin import UserLogin
from repositories.user import UserRepository
from core.Session import Session


class UserService:

    def get_links_users(self):
        user_session = Session().get_session()
        links = parametric_service.get_links()
        if user_session.is_admin:
            return links
        else:
            return [link for link in links if not link[3]]

    def create_admin_user(self, new_admin):
        self.validate_user(new_user_normal)
        new_user = UserLogin.from_dict(new_admin)
        new_user.is_admin = True
        return UserRepository.save_new_user(new_user)

    def create_normal_user(self, new_user_normal):
        self.validate_user(new_user_normal)
        new_user = UserLogin.from_dict(new_user_normal)
        return UserRepository.save_new_user(new_user)

    def validate_user(self, user):
        empty_values = False
        for entry in dict(user).items():
            if entry[1] == "" or entry[1] is None:
                empty_values = True
        if empty_values:
            raise RuntimeError("Existen campos sin llenar o invalidos")

        if not user['password'] == user['repeat_password']:
            raise RuntimeError("Las contraseñas no coinciden")

        user_exists = UserRepository.get_user_by_username(user['username'])
        if user_exists is not None:
            raise RuntimeError("El usuario existe")

    def subscribe_to_tour(self, activity):
        user = Session().get_session()
        userdb = UserRepository.find_by_id(user.id)
        pass


user_service = UserService()
