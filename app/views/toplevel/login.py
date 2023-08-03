import customtkinter as ctk
from core.Core import Core
from controllers.LoginController import LoginController
from CTkMessagebox import CTkMessagebox
import tkinter as tk


class LoginView:

    def __init__(self, root):
        self.root = root
        self.login = tk.Toplevel(master=root)
        self.login.title("Iniciar sesión")
        self.login.resizable(False, False)
        self.login.geometry("300x400")
        self.login.focus_force()

        self.login.update_idletasks()
        ancho = self.login.winfo_width()
        alto = self.login.winfo_height()
        x = (self.login.winfo_screenwidth() - ancho) // 2
        y = (self.login.winfo_screenheight() - alto) // 2
        self.login.geometry(f"{ancho}x{alto}+{x}+{y}")

        # self.login.attributes("-type", "dialog")

        frame = ctk.CTkFrame(self.login)
        frame.pack(padx=0, pady=0, fill="both", expand=True)

        label = ctk.CTkLabel(frame, text="Iniciar sesión", font=("Roboto", 30))
        label.pack(pady=20)

        label_username = ctk.CTkLabel(frame, text="Usuario:")
        label_username.pack(pady=5)
        self.entry_username = ctk.CTkEntry(frame)
        self.entry_username.pack(pady=5)

        label_password = ctk.CTkLabel(frame, text="Contraseña:")
        label_password.pack(pady=5)
        self.entry_password = ctk.CTkEntry(frame, show="*")
        self.entry_password.pack(pady=5)

        login_button = ctk.CTkButton(
            frame, text="Iniciar sesión", command=self.do_login)
        login_button.pack(pady=20)

        self.error_label = ctk.CTkLabel(frame, text="", text_color="red")
        self.error_label.pack(pady=5)

    def do_login(self):
        username = self.entry_username.get()
        user_password: str = self.entry_password.get()
        if username == "" or user_password == "":
            self.show_error_message("Rellene todos los campos")
        else:
            result = LoginController.sign_in(username=username, password=user_password)
            if result:
                self.login.destroy()
                self.root.destroy()
                Core.open_controller('home')
            else:
                CTkMessagebox(title="Error", message="Usuario o Contraseña incorrectos", icon="cancel")
                return

    def show_error_message(self, message):
        self.error_label.configure(text=message)
