import math

import customtkinter as ctk
from tkinter.font import BOLD
from tkcalendar import Calendar, DateEntry
import tkinter as tk
from config import CONFIG


def generate_form(parent, fields):
    frame = ctk.CTkFrame(parent, fg_color='transparent')
    frame.pack(expand=True, fill=ctk.BOTH)

    for i, entry in enumerate(fields):
        control = ctk.CTkFrame(frame, fg_color='transparent')
        label = ctk.CTkLabel(control, text=entry['label'].upper())
        label.pack(pady=5)

        input_control = None
        if entry['type'] == 'date':
            input_control = DateEntry(control, width=12, background='darkblue', foreground='white', borderwidth=2)
        elif entry['type'] == 'password':
            input_control = ctk.CTkEntry(control, placeholder_text=entry['placeholder'], show="*")
        else:
            input_control = ctk.CTkEntry(control, placeholder_text=entry['placeholder'])

        input_control.pack(pady=5)

        parent.form.append((entry['field'], input_control))
        control.grid(row=i // 3, column=i % 3, padx=10, pady=10, ipadx=10, ipady=10)

        for index in range(3):
            control.columnconfigure(index, weight=1)

        for index in range((len(fields) + 2) // 3):
            control.rowconfigure(index, weight=1)
    return frame


def ordenate_label(parent, fields):
    frame = ctk.CTkScrollableFrame(parent, fg_color='transparent', corner_radius=10, label_anchor=ctk.CENTER)
    frame.pack(expand=True, fill=ctk.BOTH, anchor=ctk.CENTER, ipadx=10, ipady=10, padx=5, pady=5)

    for i, entry in enumerate(fields):
        control = ctk.CTkFrame(frame, fg_color='transparent')
        label = ctk.CTkLabel(control, text=entry['label'].upper(), font=(CONFIG['font-family'], 15, BOLD))
        label.pack(pady=5, anchor=ctk.CENTER)
        input_control = ctk.CTkLabel(control, text=entry['value'])
        input_control.pack(pady=5, anchor=ctk.CENTER)
        control.grid(row=i // 3, column=i % 3, padx=10, pady=10, ipadx=10, ipady=10)
    return frame


def generate_stars(parent, popularity):
    frame = ctk.CTkFrame(parent, fg_color="transparent", height=10)

    stars_full = math.floor(popularity)
    total_stars = 5

    for i in range(stars_full):
        star_full = ctk.CTkLabel(frame, text='★', text_color="yellow", font=(CONFIG['font-family'], 30))
        star_full.grid(row=0, column=i, sticky='nsew')

    for i in range(stars_full, total_stars):
        star_empty = ctk.CTkLabel(frame, text='☆', text_color="yellow", font=(CONFIG['font-family'], 30))
        star_empty.grid(row=0, column=i, sticky='nsew')

    return frame
