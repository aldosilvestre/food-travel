from core.Controller import Controller


class LoginController(Controller):
    def __init__(self):
        self.login = self.loadView("login")

    def main(self):
        self.login.main()

    def signIn(self, username, password):
        print(username)
        print(password)
        return False
