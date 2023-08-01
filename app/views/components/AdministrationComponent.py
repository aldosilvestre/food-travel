from views.components.Component import Component
import customtkinter as ctk
from controllers.DestinationController import DestinationController
from utils.form import generate_form
from views.toplevel.funcionalities.Operations import operations


class AdministrationComponent(Component):
    botones = {
        'Crear Destino': operations.create_destiny,
        'Crear Usuario Admin': operations.create_admin_user,
        'Eliminar Destino': lambda: print,
        'Eliminar Usuario': lambda: print,
        'Centrar Mapa': lambda: print,
    }

    num_columns = 3

    def __init__(self, container, last_frame=None):
        super().__init__(container, last_frame)

        label = ctk.CTkLabel(self, text="Consola Administración", font=("Roboto", 25))
        label.pack(padx=10, pady=10, anchor=ctk.CENTER)

        frame_content = ctk.CTkFrame(self)
        frame_content.pack(expand=True, fill=ctk.BOTH, anchor='center')

        for index, texto_boton in enumerate(self.botones):
            button = ctk.CTkButton(
                master=frame_content,
                text=texto_boton,
                height=30,
                width=200,
                command=self.botones[texto_boton]
            )
            button.grid(row=index // self.num_columns, column=index % self.num_columns, padx=5, pady=5, sticky='nsew')

        for i in range(self.num_columns):
            frame_content.columnconfigure(i, weight=1)

        for i in range((len(self.botones) + 2) // self.num_columns):
            frame_content.rowconfigure(i, weight=1)

        self.main()
