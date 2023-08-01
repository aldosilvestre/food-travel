from views.components.Component import Component
import customtkinter as ctk
import base64
from tkinter.font import BOLD
import tkintermapview as map
from controllers.DestinationController import DestinationController
from services.parametrics_service import parametric_service
from PIL import ImageTk, Image
import requests
import io


class MapComponent(Component):

    def __init__(self, container, last_frame=None):
        super().__init__(container, last_frame)

        self.controller = DestinationController()
        self.destinies = self.controller.get_all()

        self.title_plain = ctk.CTkLabel(self, text='Explorar', font=('Roboto', 30, BOLD))
        self.title_plain.pack(padx=5, pady=5, ipady=15, fill=ctk.X)

        self.contentFrame = ctk.CTkFrame(self)
        self.contentFrame.pack(padx=5, pady=5, expand=True, fill=ctk.BOTH)

        self.contentFrame.grid_columnconfigure(0, weight=1)
        self.contentFrame.grid_columnconfigure(1, weight=1)
        self.contentFrame.grid_rowconfigure(0, weight=1)

        self.left_widget = ctk.CTkFrame(self.contentFrame, corner_radius=5)
        self.left_widget.grid(row=0, column=0, padx=5, pady=5, sticky='nsew')

        self.filter_widget = ctk.CTkFrame(self.left_widget, height=50, corner_radius=5)
        self.filter_widget.pack(expand=True, fill=ctk.BOTH, ipadx=5, ipady=5)

        self.entry = ctk.CTkEntry(self.filter_widget)
        self.entry.pack(fill=ctk.X, expand=True)

        button = ctk.CTkButton(self.filter_widget, text="Buscar", command=lambda: self.search())
        button.pack(fill=ctk.X, expand=True, anchor='center')

        self.map_widget = ctk.CTkFrame(self.left_widget, corner_radius=5)
        self.map_widget.pack(expand=True, fill=ctk.BOTH, ipadx=5, ipady=5)

        self.description_widget = ctk.CTkFrame(self.contentFrame, width=500, corner_radius=5)
        self.description_widget.grid(row=0, column=1, padx=5, pady=5, sticky='nsew')
        self.description_widget.label = None

        self.map_destinies = map.TkinterMapView(self.map_widget, width=1000, height=700, corner_radius=10, max_zoom=17)
        self.map_destinies.set_zoom(14)
        self.map_destinies.pack(fill="both", expand=True)

        center = parametric_service.get_center_map()
        self.map_destinies.set_position(center[0], center[1], marker=False)
        self.markers = []
        self.load_body()

        self.main()

    def search(self):
        self.clean_markers()
        if len(self.entry.get()) > 0:
            self.destinies = self.controller.get_by_address(self.entry.get())
        else:
            self.destinies = self.controller.get_all()
        self.load_body()


    def load_body(self):
        for destiny in self.destinies:
            self.markers.append(self.map_destinies.set_marker(destiny.ubication.coordinates[0], destiny.ubication.coordinates[1],
                                          text=destiny.name, data=destiny,
                                          command=lambda it=destiny: self.marker_click(it)))

    def marker_click(self, marker):
        if self.description_widget.label is not None:
            self.description_widget.label.destroy()

        imagen = self.load_image(marker.data.image)

        if imagen:
            self.description_widget.label = ctk.CTkLabel(self.description_widget, text="", image=imagen,
                                                         corner_radius=10)
            self.description_widget.label.pack(padx=10, pady=10)
        else:
            self.description_widget.label = ctk.CTkLabel(self.description_widget,
                                                         text="Error al cargar la imagen desde la URL.")
            self.description_widget.label.pack()

    def load_image(self, url):
        try:
            response = requests.get(url)
            imagen = Image.open(io.BytesIO(response.content))
            return ctk.CTkImage(imagen, size=(500, 400))
        except Exception as e:
            print("Error al cargar la imagen:", e)
            return None

    def clean_markers(self):
        for marker in self.markers:
            marker.delete()
