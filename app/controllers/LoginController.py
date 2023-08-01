from core.Controller import Controller
from services.login_service import sign_in

class LoginController(Controller):
    def __init__(self):
        self.login = self.loadView("login")

    def main(self):
        self.login.main()

    @staticmethod
    def sign_in(username, password):
        return sign_in(username, password)
