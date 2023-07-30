import customtkinter as ctk
from tkinter.font import BOLD
from PIL import Image
from app.config import getResource

from app.core.Core import Core


class HomeView(ctk.CTk):
    font_title = ("Magneto", 60, BOLD)

    def __init__(self, controller):
        super().__init__()

        self.title("Home")
        self.geometry("1280x720")
        # self.resizable(False, False)

        self.links = controller.user_links

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.navigation_frame = ctk.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(len(self.links), weight=1)
        self.content_frame = ctk.CTkFrame(self, corner_radius=0)
        self.content_frame.grid(row=0, column=1, sticky="nsew")
        self.actual_frame = Core.openComponent('tour', container=self.content_frame)
        self.load_sidebar()

    def load_sidebar(self):
        row_index = 0
        for link in self.links:
            icon = ctk.CTkImage(Image.open(getResource(f"img/{link[2]}.png")), size=(30, 30))

            frame = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10,
                                  text=link[0],
                                  fg_color="transparent", text_color=("gray10", "gray90"),
                                  hover_color=("gray70", "gray30"),
                                  image=icon, anchor="w",
                                  command=lambda param=link: self.change_frame(param[1])
                                  )
            frame.grid(row=row_index, column=0, sticky="ew")
            row_index += 1

    def change_frame(self, component):
        self.actual_frame = Core.openComponent(component, container=self.content_frame, last_frame=self.actual_frame)

    def main(self):
        self.mainloop()
