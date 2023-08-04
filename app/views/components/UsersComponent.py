from views.components.Component import Component
import customtkinter as ctk
from tkinter.font import BOLD
from controllers.UserController import user_controller
from config import CONFIG
from utils.form import ordenate_label
from CTkMessagebox import CTkMessagebox

class UsersComponent(Component):
    def __init__(self, container, last_frame=None):
        super().__init__(container, last_frame)

        self.users = user_controller.get_all()

        self.contentFrame = ctk.CTkFrame(self)
        self.contentFrame.pack(padx=5, pady=5, expand=True, fill=ctk.BOTH)

        self.contentFrame.grid_columnconfigure(0, weight=1)
        self.contentFrame.grid_columnconfigure(1, weight=1)
        self.contentFrame.grid_rowconfigure(0, weight=1)

        self.users_frame = ctk.CTkFrame(self.contentFrame, corner_radius=5)
        self.users_frame.grid(row=0, column=0, padx=5, pady=5, sticky='nsew')

        self.info_frame = ctk.CTkFrame(self.contentFrame, corner_radius=5)
        self.info_frame.grid(row=0, column=1, padx=5, pady=5, sticky='nsew')


        ### carga widget usuario ###
        self.title_activity = ctk.CTkLabel(self.users_frame, text='Usuarios',
                                           font=(CONFIG['font-family'], 30, BOLD))
        self.title_activity.pack(padx=5, pady=5, ipady=15, fill=ctk.X)

        self.widget_users = ctk.CTkScrollableFrame(self.users_frame)
        self.widget_users.pack(padx=5, pady=5, expand=True, fill=ctk.BOTH)

        self.frame_user = None

        self.load_users()

        ## fin de carga usuarios

        self.frame_info = ctk.CTkFrame(self.info_frame)
        self.frame_info.pack(expand=True, fill=ctk.BOTH)

        self.description_widget = ctk.CTkFrame(self.frame_info, width=500, corner_radius=5)
        self.description_widget.grid(row=0, column=1, padx=5, pady=5, sticky='nsew')

        self.description_widget.grid_rowconfigure(0, weight=1)
        self.description_widget.grid_rowconfigure(1, weight=1)
        self.description_widget.grid_rowconfigure(2, weight=1)
        self.description_widget.grid_columnconfigure(0, weight=1)

        self.description_widget.info = None

        self.main()

    def load_users(self):
        if self.frame_user is not None:
            self.frame_user.destroy()

        self.frame_user = ctk.CTkFrame(self.widget_users)
        self.frame_user.pack(fill=ctk.BOTH, expand=True, padx=5, pady=5)

        for user in self.users:
            button = ctk.CTkButton(self.frame_user, text=user.name, fg_color='transparent',
                                   text_color=('black', 'white'), hover_color=CONFIG['color-secondary'],
                                   font=(CONFIG['font-family'], 15, BOLD), anchor='w',
                                   command=lambda it=user: self.select_user(it))
            button.pack(fill=ctk.BOTH, expand=True, padx=5, pady=(0, 10), ipadx=5, ipady=10, anchor='w')

    def select_user(self, user):
        if self.description_widget.info is not None:
            self.description_widget.destroy()

        self.description_widget = ctk.CTkFrame(self.contentFrame, width=500, corner_radius=5)
        self.description_widget.grid(row=0, column=1, padx=5, pady=5, sticky='nsew')

        fields = [
            {"label": 'Nombre', "value": user.name},
            {"label": 'Apeliido', "value": user.last_name},
            {"label": 'Usuario', "value": user.username},
        ]

        self.description_widget.info = ordenate_label(self.description_widget, fields)
        self.description_widget.info.pack(fill=ctk.BOTH, expand=True, anchor='center')

        button_subscribe = ctk.CTkButton(self.description_widget, text='Eliminar',
                                         command=lambda it=user: self.delete(it))
        button_subscribe.pack(expand=True, fill=ctk.X, anchor='center', ipady=10)

    def delete(self, user):
        try:
            user_controller.delete_user(user)
            CTkMessagebox(title="Exito", message="Se borro el usuario", icon="info")
            self.load_users()
        except RuntimeError as e:
            CTkMessagebox(title="Error", message="No se logro borrar el usuario", icon="cancel")
