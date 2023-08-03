from views.components.Component import Component
import customtkinter as ctk
from controllers.DestinationController import destination_controller
from utils.form import generate_form
from config import CONFIG
from CTkMessagebox import CTkMessagebox


class NewDestinyComponent(Component):
    entries = [
        {'field': 'name', 'label': 'Nombre destino', 'placeholder': 'Ingrese nombre local', 'type': 'string'},
        {'field': 'type', 'label': 'Tipo Destino', 'placeholder': 'Ingrese tipo de comida', 'type': 'string'},
        {'field': 'min_price', 'label': 'Precio minimo', 'placeholder': 'Ingrese el precio minimo', 'type': 'float'},
        {'field': 'max_price', 'label': 'Precio maximo', 'placeholder': 'Ingrese el precio maximo', 'type': 'float'},
        {'field': 'ingredients', 'label': 'Ingredientes', 'placeholder': 'Separe por comas (,)', 'type': 'bool'},
        {'field': 'disponibility', 'label': 'Disponible', 'placeholder': 'Ingrese Si o No', 'type': 'bool'},
        {'field': 'address', 'label': 'Dirección', 'placeholder': 'Ingrese tipo la dirección', 'type': 'string'},
        {'field': 'ubication_latitude', 'label': 'Latitud', 'placeholder': 'Ingrese la latitud', 'type': 'float'},
        {'field': 'ubication_longitude', 'label': 'Longitud', 'placeholder': 'Ingrese la longitud', 'type': 'float'},
        {'field': 'image', 'label': 'Imagen', 'placeholder': 'Ingrese el link', 'type': 'string'}
    ]

    def __init__(self, container, last_frame=None):
        super().__init__(container, last_frame)
        self.controller = destination_controller
        self.form = []

        label = ctk.CTkLabel(self, text="Nuevo Destino", font=(CONFIG['font-family'], 25))
        label.pack(padx=10, pady=10, anchor=ctk.CENTER)

        self.load_form()

        button = ctk.CTkButton(self, text='Guardar', command=lambda: self.guardar_nuevo())
        button.pack(padx=10, pady=20)

        self.main()

    def load_form(self):
        generate_form(self, self.entries)

    def guardar_nuevo(self):
        try:
            new_destiny = {entry[0]: entry[1].get() for entry in self.form}
            self.controller.new_destiny(new_destiny)
            self.container.destroy()
            CTkMessagebox(title="Exito", message="Se guardo correctamente", icon="info")
        except RuntimeError as e:
            CTkMessagebox(title="Error", message="No se guardo el destino", icon="cancel")
