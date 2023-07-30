from core.Controller import Controller


class DashboardController(Controller):

    def __init__(self):
        self.dashboard = self.loadView("dashboard")
        self.main()

    def main(self):
        self.dashboard.main()
