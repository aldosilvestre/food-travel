from services.user_service import user_service


class UserController:

    def create_new_user(self, new_user):
        return user_service.create_normal_user(new_user)

    def create_new_admin(self, new_user):
        return user_service.create_admin_user(new_user)

    def subscribe(self, activity):
        return user_service.subscribe_to_tour(activity)


user_controller = UserController()
