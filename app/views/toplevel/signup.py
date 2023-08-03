import customtkinter as ctk
import tkinter as tk
from tkinter.font import BOLD
from controllers.UserController import user_controller
from utils.form import generate_form
from config import CONFIG
from CTkMessagebox import CTkMessagebox

class SignupView(tk.Toplevel):

    entries = [
        {'field': 'username', 'label': 'Nombre Usuario', 'placeholder': 'Ingrese nombre de usuario', 'type': 'string'},
        {'field': 'name', 'label': 'Nombre', 'placeholder': 'Ingrese su nombre', 'type': 'string'},
        {'field': 'last_name', 'label': 'Apellido', 'placeholder': 'Ingrese su apellido', 'type': 'string'},
        {'field': 'password', 'label': 'Contraseña', 'placeholder': 'Ingrese nombre la contraseña', 'type': 'password'},
        {'field': 'repeat_password', 'label': 'Repita Contraseña', 'placeholder': 'Repita la contraseña', 'type': 'password'},
    ]

    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.geometry("600x350")
        self.resizable(False, False)

        self.update_idletasks()
        ancho = self.winfo_width()
        alto = self.winfo_height()
        x = (self.winfo_screenwidth() - ancho) // 2
        y = (self.winfo_screenheight() - alto) // 2
        self.geometry(f"{ancho}x{alto}+{x}+{y}")

        self.content = ctk.CTkFrame(self)
        self.content.pack(expand=True, fill=ctk.BOTH)

        self.content.form = []

        label = ctk.CTkLabel(self.content, text="Registrarse", font=(CONFIG['font-family'], 25))
        label.pack(padx=10, pady=10, anchor=ctk.CENTER)

        generate_form(self.content, self.entries)

        button = ctk.CTkButton(self.content, text='Registrarse', command=lambda: self.guardar_nuevo())
        button.pack(padx=10, pady=20)

    def guardar_nuevo(self):
        try:
            new_admin = {entry[0]: entry[1].get() for entry in self.content.form}
            user_controller.create_new_user(new_admin)
            self.destroy()
            CTkMessagebox(title="Exito", message="Se creo correctamente", icon="info")
        except RuntimeError as e:
            mensaje = e.args[0] if len(e.args) > 0 else "No se creo el usuario"
            CTkMessagebox(title="Error", message=mensaje, icon="cancel")

