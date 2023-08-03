from views.components.Component import Component
import customtkinter as ctk
from controllers.UbicationController import ubication_controller
from utils.form import generate_form
from config import CONFIG


class CenterMapComponent(Component):
    entries = [
        {'field': 'name', 'label': 'Nombre Actividad', 'type': 'string'},
        {'field': 'date', 'label': 'Fecha', 'type': 'date'}
    ]

    def __init__(self, container, last_frame=None):
        super().__init__(container, last_frame)
        self.controller = ubication_controller
        self.form = []

        label = ctk.CTkLabel(self, text="Centrar ubicacion", font=(CONFIG['font-family'], 25))
        label.pack(padx=10, pady=10, anchor=ctk.CENTER)

        self.load_form()

        button = ctk.CTkButton(self, text='Guardar', command=lambda: self.guardar_nuevo())
        button.pack(padx=10, pady=20)

        self.main()

    def load_form(self):
        generate_form(self, self.entries)

    def guardar_nuevo(self):
        self.controller.new_activity(name='playa', type='comida', ingredients=['pollo', 'aji'], min_price=15.52)
