from core.Controller import Controller
from services.user_service import get_links_users


class HomeController(Controller):

    def __init__(self):
        self.user_links = get_links_users()
        self.home = self.load_view("home")

    def main(self):
        self.home.main()
