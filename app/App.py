import customtkinter as ctk
# import importlib
# import os
from core.Core import Core


class App:
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("green")

    @staticmethod
    def run():
        # root = DashboardController()
        app = Core.openController("dashboard")
        # root = ctk.CTk()
        # root.resizable(False, False)
        # HomeView(root)


def main():
    App.run()
    return 0


if __name__ == "__main__":
    import sys

    sys.exit(main())
