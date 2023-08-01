import customtkinter as ctk


def generate_form(parent, fields):
    frame = ctk.CTkFrame(parent, fg_color='transparent')
    frame.pack(expand=True, fill=ctk.BOTH)

    for i, entry in enumerate(fields):
        control = ctk.CTkFrame(frame, fg_color='transparent')
        label = ctk.CTkLabel(control, text=entry['label'].upper())
        label.pack(pady=5)
        input_control = ctk.CTkEntry(control)
        input_control.pack(pady=5)
        parent.form.append((entry['field'], input_control))
        control.grid(row=i // 3, column=i % 3, padx=10, pady=10, ipadx=10, ipady=10)

        for index in range(3):
            control.columnconfigure(index, weight=1)

        for index in range((len(fields) + 2) // 3):
            control.rowconfigure(index, weight=1)

    return frame
