from services.user_service import user_service


class UserController:

    def get_all(self):
        return user_service.get_all()

    def create_new_user(self, new_user):
        return user_service.create_normal_user(new_user)

    def create_new_admin(self, new_user):
        return user_service.create_admin_user(new_user)

    def delete_user(self, user):
        return user_service.delete(user)


user_controller = UserController()
