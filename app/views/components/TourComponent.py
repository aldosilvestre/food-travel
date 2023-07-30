from app.views.components.Component import Component
import customtkinter as ctk
from tkinter.font import BOLD
import random

class TourComponent(Component):

    def __init__(self, container, last_frame=None):
        super().__init__(container, last_frame)

        self.title_activity = ctk.CTkLabel(self, text='Actividades', font=('Roboto', 30, BOLD))
        self.title_activity.pack(padx=5, pady=5, ipady=15, fill=ctk.X)

        self.widget_activity = ctk.CTkScrollableFrame(self)
        self.widget_activity.pack(padx=5, pady=5, expand=True, fill=ctk.BOTH)

        self.load_activities()

        self.title_destiny = ctk.CTkLabel(self, text='Destinos', font=('Roboto', 30, BOLD))
        self.title_destiny.pack(padx=5, pady=5, ipady=15, fill=ctk.X)

        self.widget_destiny = ctk.CTkScrollableFrame(self)
        self.widget_destiny.pack(padx=5, pady=5, expand=True, fill=ctk.BOTH)

        self.show_destinies = None

        self.main()

    def load_activities(self):
        frame_activities = ctk.CTkFrame(self.widget_activity)
        frame_activities.pack(fill=ctk.BOTH, expand=True, padx=5, pady=5)

        for i in range(20, 40):
            button = ctk.CTkButton(frame_activities, text=f"Item {i}", fg_color='green', font=('Roboto', 15, BOLD), anchor='w',
                                   command=lambda it=i: self.select_activity(it))
            button.pack(fill=ctk.BOTH, expand=True, padx=5, pady=(0, 10), ipadx=5, ipady=10, anchor='w')

    def select_activity(self, item):
        if self.show_destinies is not None:
            self.show_destinies.destroy()

        self.show_destinies = ctk.CTkFrame(self.widget_destiny)
        self.show_destinies.pack(fill=ctk.BOTH, expand=True, padx=5, pady=5)

        for i in range(1, random.randint(5, 10)):
            label = ctk.CTkLabel(self.show_destinies, text=f"Item {i}", fg_color='blue', font=('Roboto', 15, BOLD), anchor='w', corner_radius=5)
            label.pack(fill=ctk.BOTH, expand=True, padx=5, pady=(0, 5), ipadx=5, ipady=5, anchor='w')
