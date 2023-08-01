import customtkinter as ctk
from core.Core import Core


class App:
    ctk.set_appearance_mode("system")
    ctk.set_default_color_theme("green")

    @staticmethod
    def run():
        Core.open_controller("dashboard")


def main():
    App.run()
    return 0


if __name__ == "__main__":
    import sys

    sys.exit(main())
