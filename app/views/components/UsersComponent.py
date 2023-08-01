from views.components.Component import Component
import customtkinter as ctk


class UsersComponent(Component):
    def __init__(self, container, last_frame=None):
        super().__init__(container, last_frame)
        label = ctk.CTkLabel(self, text="Usuarios", font=("Roboto", 25))
        label.pack(padx=10, pady=10, anchor=ctk.CENTER)
        self.main()
