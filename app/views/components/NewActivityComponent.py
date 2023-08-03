from views.components.Component import Component
import customtkinter as ctk
from controllers.ActivityController import activity_controller
from controllers.DestinationController import destination_controller
from utils.form import generate_form
from config import CONFIG
from tkcalendar import Calendar, DateEntry
from tkinter import ttk
import tkinter as tk
from datetime import datetime
from CTkMessagebox import CTkMessagebox


class NewActivityComponent(Component):

    def __init__(self, container, last_frame=None):
        super().__init__(container, last_frame)
        container.geometry("400x500")

        self.controller = activity_controller
        self.destinies = destination_controller.get_all()

        label = ctk.CTkLabel(self, text="Nueva Actividad", font=(CONFIG['font-family'], 25))
        label.pack(padx=10, pady=10, anchor=ctk.CENTER)

        self.load_form()

        button = ctk.CTkButton(self, text='Guardar', command=lambda: self.guardar_nuevo())
        button.pack(padx=10, pady=20)

        self.main()

    def load_form(self):
        self.form = ctk.CTkFrame(self, fg_color="transparent")

        self.name = self.input_name(self.form)
        self.destiny = self.input_destiny(self.form)
        self.datetime = self.input_datetime(self.form)

        self.form.pack(expand=True, fill=ctk.BOTH)

    def input_name(self, container):
        control = ctk.CTkFrame(container, fg_color="transparent")
        label = ctk.CTkLabel(control, text='Nombre')
        label.pack(pady=5)
        self.input_control_name = ctk.CTkEntry(control, placeholder_text='Ingrese el nombre de la actividad')
        self.input_control_name.pack(pady=5)
        control.pack(expand=True, fill=ctk.BOTH)

    def input_destiny(self, container):
        control = ctk.CTkFrame(container, fg_color="transparent")
        label = ctk.CTkLabel(control, text='Destino')
        label.pack(pady=5)
        self.selected_id = tk.StringVar()
        input_destiny = ctk.CTkOptionMenu(control, variable=self.selected_id,
                                          values=[item.name for item in self.destinies])
        input_destiny.pack(pady=5)
        control.pack(expand=True, fill=ctk.BOTH)

        self.selected_id.trace('w', self.on_option_selected)

    def input_datetime(self, container):
        control = ctk.CTkFrame(container, fg_color="transparent")
        label = ctk.CTkLabel(control, text='Fecha')
        label.pack(pady=5)
        self.input_date = ctk.CTkEntry(control, placeholder_text='dd/mm/aaaa')
        self.input_date.pack(pady=5)
        control.pack(expand=True, fill=ctk.BOTH)

        control = ctk.CTkFrame(container, fg_color="transparent")
        label = ctk.CTkLabel(control, text='Hora')
        label.pack(pady=5)
        self.input_hour = tk.StringVar()
        input_hour = ttk.Spinbox(control, values=[i for i in range(0, 23)], textvariable=self.input_hour, wrap=True)
        input_hour.pack(pady=5)
        control.pack(expand=True, fill=ctk.BOTH)

        control = ctk.CTkFrame(container, fg_color="transparent")
        label = ctk.CTkLabel(control, text='Minutos')
        label.pack(pady=5)
        self.input_minutes = tk.StringVar()
        input_minutes = ttk.Spinbox(control, values=(0, 30), textvariable=self.input_minutes, wrap=True)
        input_minutes.pack(pady=5)
        control.pack(expand=True, fill=ctk.BOTH)

    def guardar_nuevo(self):
        name = self.input_control_name.get()
        destiny = self.input_control_destiny
        date = self.input_date.get()
        hour = self.input_hour.get()
        minutes = self.input_minutes.get()

        new_date = datetime.strptime(date, '%d/%m/%Y')
        new_date = new_date.replace(hour=int(hour), minute=int(minutes))

        try:
            self.controller.new_activity(name=name, destiny_id=destiny, datetime=new_date)
            CTkMessagebox(title="Exito", message="Se guardo correctamente", icon="info")
            self.container.destroy()
        except RuntimeError as e:
            CTkMessagebox(title="Error", message="No se guardo la actividad", icon="cancel")

    def on_option_selected(self, *event):
        selected_item = next(item for item in self.destinies if item.name == self.selected_id.get())
        self.input_control_destiny = selected_item.id
