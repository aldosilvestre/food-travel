from app.views.components.Component import Component
import customtkinter as ctk
from tkinter.font import BOLD
from app.controllers.PlainController import PlainController


class PlainComponent(Component):

    def __init__(self, container, last_frame=None):
        super().__init__(container, last_frame)

        self.controller = PlainController()

        self.title_plain = ctk.CTkLabel(self, text='Planificar', font=('Roboto', 30, BOLD))
        self.title_plain.pack(padx=5, pady=5, ipady=15, fill=ctk.X)

        self.contentFrame = ctk.CTkFrame(self)
        self.contentFrame.pack(padx=5, pady=5, expand=True, fill=ctk.BOTH)

        self.contentFrame.grid_columnconfigure(0, weight=1)
        self.contentFrame.grid_columnconfigure(1, weight=1)
        self.contentFrame.grid_rowconfigure(0, weight=1)

        self.destinies = ctk.CTkFrame(self.contentFrame, corner_radius=5)
        self.destinies.grid(row=0, column=0, padx=5, pady=5, sticky='nsew')

        self.actual_plan = ctk.CTkFrame(self.contentFrame, corner_radius=5)
        self.actual_plan.grid(row=0, column=1, padx=5, pady=5, sticky='nsew')

        print(self.controller.getDestinies())

        self.main()
