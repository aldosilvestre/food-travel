import customtkinter as ctk
# import importlib
# import os
# from core.Core import Core
from views.home import HomeView


# class App:
#     def __init__(self):
#         customtkinter.set_appearance_mode("System")
#         customtkinter.set_default_color_theme("blue")
#         self.root = customtkinter.CTk()
#
#     def button_function(self):
#         print("button pressed")
#
#     def run(self):
#         self.root.geometry("400x240")
#
#         frame = customtkinter.CTkFrame(master=self.root).grid()
#         self.button = customtkinter.CTkButton(
#             frame, text="CTkButton", command=(self.button_function))
#         self.button.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)
#         self.root.mainloop()
#


class App:

    ctk.set_appearance_mode("system")
    ctk.set_default_color_theme("green")

    @staticmethod
    def run():
        root = ctk.CTk()
        root.resizable(False, False)
        HomeView(root)
        root.mainloop()


def main():
    App.run()
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
