from views.components.Component import Component
import customtkinter as ctk
from controllers.UserController import user_controller
from utils.form import generate_form
from config import CONFIG
from CTkMessagebox import CTkMessagebox


class NewAdminComponent(Component):
    entries = [
        {'field': 'username', 'label': 'Nombre Usuario', 'placeholder': 'Ingrese nombre de usuario', 'type': 'string'},
        {'field': 'name', 'label': 'Nombre', 'placeholder': 'Ingrese su nombre', 'type': 'string'},
        {'field': 'last_name', 'label': 'Apellido', 'placeholder': 'Ingrese su apellido', 'type': 'string'},
        {'field': 'password', 'label': 'Contraseña', 'placeholder': 'Ingrese nombre la contraseña', 'type': 'password'},
        {'field': 'repeat_password', 'label': 'Repita Contraseña', 'placeholder': 'Repita la contraseña', 'type': 'password'},
    ]

    def __init__(self, container, last_frame=None):
        super().__init__(container, last_frame)
        self.controller = user_controller
        self.form = []

        label = ctk.CTkLabel(self, text="Nuevo Usuario Administrador", font=(CONFIG['font-family'], 25))
        label.pack(padx=10, pady=10, anchor=ctk.CENTER)

        self.load_form()

        button = ctk.CTkButton(self, text='Guardar', command=lambda: self.guardar_nuevo())
        button.pack(padx=10, pady=20)

        self.main()

    def load_form(self):
        generate_form(self, self.entries)

    def guardar_nuevo(self):
        try:
            new_admin = {entry[0]: entry[1].get() for entry in self.form}
            self.controller.create_new_admin(new_admin)
            self.container.destroy()
            CTkMessagebox(title="Exito", message="Se creo correctamente", icon="info")
        except RuntimeError as e:
            CTkMessagebox(title="Error", message="No se creo el usuario", icon="cancel")
