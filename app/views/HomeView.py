import customtkinter as ctk
from tkinter.font import BOLD
from PIL import Image
from config import get_resource

from core.Core import Core


class HomeView(ctk.CTk):

    def __init__(self, controller):
        super().__init__()

        self.title("Foodie Tour")
        self.geometry("1280x720")
        self.iconbitmap(get_resource("img/icon.ico"))
        # self.resizable(False, False)

        self.links = controller.user_links

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.navigation_frame = ctk.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(len(self.links) + 1, weight=1)
        self.content_frame = ctk.CTkFrame(self, corner_radius=0)
        self.content_frame.grid(row=0, column=1, sticky="nsew")
        self.actual_frame = Core.open_component('tour', container=self.content_frame)
        self.load_sidebar()

        self.lower()
        self.main()

    def load_sidebar(self):
        icon_avatar = ctk.CTkImage(Image.open(get_resource(f"img/home-2.png")), size=(200, 200))
        bg_image_label = ctk.CTkLabel(master=self.navigation_frame, text="", image=icon_avatar)
        bg_image_label.grid(row=0, column=0, sticky="we")

        row_index = 1
        for link in self.links:
            icon = ctk.CTkImage(Image.open(get_resource(f"img/{link[2]}.png")), size=(30, 30))

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
        self.actual_frame = Core.open_component(component, container=self.content_frame, last_frame=self.actual_frame)

    def main(self):
        self.mainloop()
