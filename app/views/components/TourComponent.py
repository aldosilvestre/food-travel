from config import CONFIG
from views.components.Component import Component
import customtkinter as ctk
from tkinter.font import BOLD
import tkintermapview as map
from controllers.TourController import TourController
from controllers.DestinationController import DestinationController


class TourComponent(Component):

    def __init__(self, container, last_frame=None):
        super().__init__(container, last_frame)

        self.controller = TourController()

        self.tour = self.controller.get_tour()

        self.contentFrame = ctk.CTkFrame(self)
        self.contentFrame.pack(padx=5, pady=5, expand=True, fill=ctk.BOTH)

        self.contentFrame.grid_columnconfigure(0, weight=1)
        self.contentFrame.grid_columnconfigure(1, weight=1)
        self.contentFrame.grid_rowconfigure(0, weight=1)

        self.tours_frame = ctk.CTkFrame(self.contentFrame, corner_radius=5)
        self.tours_frame.grid(row=0, column=0, padx=5, pady=5, sticky='nsew')

        self.destinies_frame = ctk.CTkFrame(self.contentFrame, corner_radius=5)
        self.destinies_frame.grid(row=0, column=1, padx=5, pady=5, sticky='nsew')

        self.title_activity = ctk.CTkLabel(self.tours_frame, text='Actividades',
                                           font=(CONFIG['font-family'], 30, BOLD))
        self.title_activity.pack(padx=5, pady=5, ipady=15, fill=ctk.X)

        self.widget_activity = ctk.CTkScrollableFrame(self.tours_frame)
        self.widget_activity.pack(padx=5, pady=5, expand=True, fill=ctk.BOTH)

        self.title_destiny = ctk.CTkLabel(self.destinies_frame, text='Destinos', font=(CONFIG['font-family'], 30, BOLD))
        self.title_destiny.pack(padx=5, pady=5, ipady=15, fill=ctk.X)

        self.show_destinies = None
        self.load_tour()

        self.main()

    def load_tour(self):
        frame_tours = ctk.CTkFrame(self.widget_activity)
        frame_tours.pack(fill=ctk.BOTH, expand=True, padx=5, pady=5)

        for activity in self.tour.activities:
            button = ctk.CTkButton(frame_tours, text=activity.name, fg_color='transparent',
                                   text_color=('black', 'white'), hover_color=CONFIG['color-secondary'],
                                   font=(CONFIG['font-family'], 15, BOLD), anchor='w',
                                   command=lambda it=activity: self.select_activity(it))
            button.pack(fill=ctk.BOTH, expand=True, padx=5, pady=(0, 10), ipadx=5, ipady=10, anchor='w')

    def select_activity(self, item):
        if self.show_destinies is not None:
            self.show_destinies.destroy()

        self.show_destinies = map.TkinterMapView(self.destinies_frame, width=400, corner_radius=10, max_zoom=17)
        self.show_destinies.set_zoom(16)
        self.show_destinies.pack(padx=5, pady=5, fill="both", expand=True)

        self.load_map()

        self.show_destinies.set_position(float(item.destiny.ubication.coordinates[0]), float(item.destiny.ubication.coordinates[1]),
                                         marker=False)

    def load_map(self):
        activities = self.tour.activities
        for activity in activities:
            destiny = activity.destiny
            self.show_destinies.set_marker(float(destiny.ubication.coordinates[0]), float(destiny.ubication.coordinates[1]),
                                           text=destiny.name, command=lambda it=activity: self.show_data(it))

        destinies = [(float(activity.destiny.ubication.coordinates[0]),(float(activity.destiny.ubication.coordinates[1]))) for activity in self.tour.activities]

        if len(destinies) > 1:
            self.show_destinies.set_path(destinies)

    def show_data(self, activity):
        print(activity)
        pass