import customtkinter as ctk


def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance


@singleton
class LoginView:

    def __init__(self, root):
        self.root = root
        self.login = ctk.CTkToplevel(root)
        self.login.title("Iniciar sesión")
        self.login.resizable(False, False)
        self.login.geometry("300x400")
        self.login.attributes("-type", "dialog")

        frame = ctk.CTkFrame(self.login)
        frame.pack(padx=20, pady=20, fill="both", expand=True)

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
        password = self.entry_password.get()
        if username != "" and password != "":
            print(username)
            print(password)
            self.login.destroy()
            self.root.success()
        else:
            self.show_error_message("Rellene todos los campos")

    def show_error_message(self, message):
        self.error_label.configure(text=message)
