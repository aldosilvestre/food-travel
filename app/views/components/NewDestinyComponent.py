from views.components.Component import Component
import customtkinter as ctk
from controllers.DestinationController import DestinationController
from utils.form import generate_form


class NewDestinyComponent(Component):
    entries = [
        {'field': 'name', 'label': 'Nombre destino', 'type': 'string'},
        {'field': 'type', 'label': 'Tipo Destino', 'type': 'string'},
        {'field': 'min_price', 'label': 'precio minimo', 'type': 'float'},
        {'field': 'max_price', 'label': 'precio maximo', 'type': 'float'},
        {'field': 'disponibility', 'label': 'Disponible', 'type': 'bool'},
        {'field': 'ubication_latitude', 'label': 'Latitud', 'type': 'float'},
        {'field': 'ubication_longitude', 'label': 'Longitud', 'type': 'float'},
        {'field': 'image', 'label': 'Imagen', 'type': 'string'}
    ]

    def __init__(self, container, last_frame=None):
        super().__init__(container, last_frame)
        self.controller = DestinationController()
        self.form = []

        label = ctk.CTkLabel(self, text="Nuevo Destino", font=("Roboto", 25))
        label.pack(padx=10, pady=10, anchor=ctk.CENTER)

        self.load_form()

        button = ctk.CTkButton(self, text='Guardar', command=lambda: self.guardar_nuevo())
        button.pack(padx=10, pady=20)

        self.main()

    def load_form(self):
        generate_form(self, self.entries)

    def guardar_nuevo(self):
        self.controller.new_destiny(name='playa', type='comida', ingredients=['pollo', 'aji'], min_price=15.52)
