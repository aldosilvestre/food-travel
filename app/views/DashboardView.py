import customtkinter as ctk
from PIL import Image
from app.config import getResource
from app.views.toplevel.login import LoginView
from app.views.toplevel.signup import SignupView
from tkinter.font import BOLD


class DashboardView(ctk.CTk):
    font_title = ("Magneto", 60, BOLD)

    def __init__(self, controller):
        super().__init__()

        self.title("Foodie Tour")
        self.geometry("1000x700")
        self.resizable(False, False)
        self.dashboard = controller

        self.container = ctk.CTkFrame(master=self)
        self.container.pack(pady=0, padx=0, fill="both", expand=True)
        self.load_header()
        self.load_body()
        self.load_footer()

    def load_header(self):
        frame_header = ctk.CTkFrame(
            master=self.container, fg_color="gray")
        frame_header.pack(side=ctk.TOP, fill=ctk.X, padx=2, pady=2)

        title = ctk.CTkLabel(frame_header, text="Bienvenido", font=("Arial", 20, BOLD))
        title.pack(padx=10, pady=10, side=ctk.LEFT)

        btn_signin = ctk.CTkButton(
            frame_header, text="Sign in", command=lambda: self.ir_a('signin'))
        btn_signin.pack(padx=10, pady=10, side=ctk.RIGHT)
        btn_signup = ctk.CTkButton(
            frame_header, text="Sign up", command=lambda: self.ir_a('signup'))
        btn_signup.pack(padx=10, pady=10, side=ctk.RIGHT)

    def ir_a(self, toplevel):
        if toplevel == 'signin':
            LoginView(self)
        else:
            SignupView(self)

    def load_body(self):
        frame_body = ctk.CTkFrame(
            master=self.container, height=600, width=1000)
        frame_body.pack(fill=ctk.X, padx=2, pady=2)
        bg_image = ctk.CTkImage(Image.open(
            getResource("img/home.jpg")), size=(1000, 600))
        bg_image_label = ctk.CTkLabel(
            master=frame_body, text="Foodie Tour", font=self.font_title, image=bg_image, text_color="light green")
        bg_image_label.pack(expand=True, fill="both")

    def load_footer(self):
        frame_footer = ctk.CTkFrame(
            master=self.container, height=100, width=1000, fg_color="blue")
        frame_footer.pack(side=ctk.BOTTOM, fill=ctk.X, padx=2, pady=2)
        label = ctk.CTkLabel(
            frame_footer, text="Foodie Tour es una marca registrada de Foodie Tour. All right reserved © 2023",
            text_color="white")
        label.pack(padx=10, pady=10)

    def main(self):
        self.mainloop()
