from views.components.Component import Component
import customtkinter as ctk
import base64
from tkinter.font import BOLD
import tkintermapview as map
from controllers.ActivityController import activity_controller
from services.parametrics_service import parametric_service
from PIL import ImageTk, Image
import requests
import io
from config import CONFIG
from utils.form import ordenate_label, generate_stars
from datetime import datetime
from controllers.UserController import user_controller

entries = [
    {'field': 'name', 'label': 'Nombre destino', 'type': 'string'},
    {'field': 'type', 'label': 'Tipo Destino', 'type': 'string'},
    {'field': 'min_price', 'label': 'precio minimo', 'type': 'float'},
    {'field': 'max_price', 'label': 'precio maximo', 'type': 'float'},
    {'field': 'disponibility', 'label': 'Disponible', 'type': 'bool'},
]


class MapComponent(Component):

    def __init__(self, container, last_frame=None):
        super().__init__(container, last_frame)

        self.activities = activity_controller.get_all()

        self.title_plain = ctk.CTkLabel(self, text='Explorar', font=(CONFIG['font-header'], 30, BOLD))
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

        self.entry = ctk.CTkEntry(self.filter_widget, placeholder_text="Ingrese la dirección a buscar")
        self.entry.pack(fill=ctk.BOTH, expand=True)

        button = ctk.CTkButton(self.filter_widget, text="Buscar", command=lambda: self.search())
        button.pack(fill=ctk.X, expand=True, anchor='center', ipady=5)

        self.map_widget = ctk.CTkFrame(self.left_widget, corner_radius=5)
        self.map_widget.pack(expand=True, fill=ctk.BOTH, ipadx=5, ipady=5)

        self.description_widget = ctk.CTkFrame(self.contentFrame, width=500, corner_radius=5)
        self.description_widget.grid(row=0, column=1, padx=5, pady=5, sticky='nsew')

        self.description_widget.grid_rowconfigure(0, weight=1)
        self.description_widget.grid_rowconfigure(1, weight=1)
        self.description_widget.grid_rowconfigure(2, weight=1)
        self.description_widget.grid_columnconfigure(0, weight=1)

        self.description_widget.label = None
        self.description_widget.image = None
        self.description_widget.info = None

        self.map_destinies = map.TkinterMapView(self.map_widget, width=1000, height=700, corner_radius=10, max_zoom=17)
        self.map_destinies.set_zoom(14)
        self.map_destinies.pack(fill="both", expand=True)

        center = parametric_service.get_center_map()
        self.map_destinies.set_position(center.value[0], center.value[1], marker=False)
        self.markers = []
        self.load_body()

        self.main()

    def search(self):
        self.clean_markers()
        if len(self.entry.get()) > 0:
            self.activities = activity_controller.get_by_address(self.entry.get())
        else:
            self.activities = activity_controller.get_all()
        self.load_body()

    def load_body(self):
        for activity in self.activities:
            self.markers.append(self.map_destinies.set_marker(float(activity.destiny.ubication.coordinates[0]),
                                                              float(activity.destiny.ubication.coordinates[1]),
                                                              text=activity.destiny.name, data=activity,
                                                              command=lambda it: self.marker_click(it)))

    def marker_click(self, marker):
        if self.description_widget.label is not None:
            self.description_widget.destroy()

        self.description_widget = ctk.CTkFrame(self.contentFrame, width=500, corner_radius=5)
        self.description_widget.grid(row=0, column=1, padx=5, pady=5, sticky='nsew')

        self.description_widget.label = ctk.CTkLabel(self.description_widget, text=marker.data.name, height=10,
                                                     fg_color='transparent',
                                                     font=(CONFIG['font-family'], 15, BOLD), corner_radius=10)
        self.description_widget.label.pack(fill=ctk.X, anchor='n', pady=10)

        self.description_widget.popularity = generate_stars(self.description_widget, marker.data.destiny.popularity)
        self.description_widget.popularity.pack(fill=ctk.X, anchor='n', padx=10)

        imagen = self.load_image(marker.data.destiny.image)

        if imagen:
            self.description_widget.image = ctk.CTkLabel(self.description_widget, text="", image=imagen, height=10,
                                                         corner_radius=10)
            self.description_widget.image.pack(padx=10, pady=10)
        else:
            self.description_widget.image = ctk.CTkLabel(self.description_widget,
                                                         text="Error al cargar la imagen desde la URL.")
            self.description_widget.image.pack()

        my_datetime = datetime.fromisoformat(str(marker.data.datetime))

        fields = [
            {"label": 'Lugar', "value": marker.data.destiny.name},
            {"label": 'Tipo', "value": marker.data.destiny.type},
            {"label": 'Fecha', "value": my_datetime.strftime('%d/%m/%Y')},
            {"label": 'Hora', "value": my_datetime.time()},
            {"label": 'Precio Minimo', "value": marker.data.destiny.min_price},
            {"label": 'Precio Maximo', "value": marker.data.destiny.max_price},
            {"label": 'Ingredientes', "value": marker.data.destiny.ingredients},
            {"label": 'Dirección', "value": marker.data.destiny.ubication.address},
        ]

        self.description_widget.info = ordenate_label(self.description_widget, fields)
        self.description_widget.info.pack(fill=ctk.BOTH, expand=True, anchor='center')

        button_subscribe = ctk.CTkButton(self.description_widget, text='SUBSCRIBIR A TOUR',
                                         command=lambda: self.subscribe(marker.data))
        button_subscribe.pack(expand=True, fill=ctk.X, anchor='center', ipady=10)

    def subscribe(self, activity):
        user_controller.subscribe(activity)

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
