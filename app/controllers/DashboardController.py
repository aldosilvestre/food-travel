from core.Controller import Controller


class DashboardController(Controller):

    def __init__(self):
        self.dashboard = self.load_view("dashboard")

    def main(self):
        self.dashboard.main()
