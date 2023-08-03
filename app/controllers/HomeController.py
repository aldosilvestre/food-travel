from core.Controller import Controller
from services.user_service import user_service


class HomeController(Controller):

    def __init__(self):
        self.user_links = user_service.get_links_users()
        self.home = self.load_view("home")

    def main(self):
        self.home.main()
