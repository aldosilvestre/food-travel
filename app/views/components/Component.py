import customtkinter as ctk


class Component(ctk.CTkFrame):
    def __init__(self, container, last_frame):
        super().__init__(container)
        if last_frame is not None:
            last_frame.destroy()

    def main(self):
        self.pack(pady=0, padx=0, fill=ctk.BOTH, expand=True)
