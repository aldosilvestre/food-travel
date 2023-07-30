from app.core.Controller import Controller
from app.services.user_service import get_links_users


class HomeController(Controller):

    def __init__(self):
        self.user_links = get_links_users()
        self.home = self.loadView("home")
        self.main()

    def main(self):
        self.home.main()
