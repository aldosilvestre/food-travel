from app.views.components.Component import Component
import customtkinter as ctk
from app.controllers.DestinationController import DestinationController


class DestinyComponent(Component):

    def __init__(self, container, last_frame=None):
        super().__init__(container, last_frame)
        self.controller = DestinationController()

        label = ctk.CTkLabel(self, text="Destino", font=("Roboto", 25))
        label.pack(padx=10, pady=10, anchor=ctk.CENTER)

        button = ctk.CTkButton(self, text='Guardar', command=lambda: self.guardar_nuevo())
        button.pack(padx=10, pady=20)

        self.main()

    def guardar_nuevo(self):
        self.controller.new_destiny(name='playa', type='comida', ingredients=['pollo', 'aji'], min_price=15.52)
