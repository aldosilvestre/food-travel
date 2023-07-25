# import customtkinter
# import importlib
# import os
from core.Core import Core

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
    @staticmethod
    def run():
        # try:
        app = Core.openController("login")
        app.main()
        # except Exception as e:
        # print(str(e))


def main():
    App.run()
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
