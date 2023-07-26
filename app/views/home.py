import customtkinter as ctk
from PIL import Image
from config import getResource
from views.login import LoginView


class HomeView:
    def __init__(self, root):
        root.title("Home")
        root.geometry("1000x700")
        self.root = root
        self.container = ctk.CTkFrame(master=root)
        self.container.pack(pady=0, padx=0, fill="both", expand=True)
        self.loadHeader()
        self.loadBody()
        self.loadFooter()

    def loadHeader(self):
        frameHeader = ctk.CTkFrame(
            master=self.container, height=50, width=1000, fg_color="gray")
        frameHeader.pack(side=ctk.TOP, fill=ctk.X, padx=2, pady=2)
        btnSignIn = ctk.CTkButton(
            frameHeader, text="Sign in", command=lambda: LoginView(self.root))
        btnSignIn.pack(padx=10, pady=10, side=ctk.RIGHT)
        btnSignUp = ctk.CTkButton(
            frameHeader, text="Sign up", command=(self.signupView))
        btnSignUp.pack(padx=10, pady=10, side=ctk.RIGHT)

    def loadBody(self):
        frameBody = ctk.CTkFrame(
            master=self.container, height=600, width=1000)
        frameBody.pack(fill=ctk.X, padx=2, pady=2)
        bgImage = ctk.CTkImage(Image.open(
            getResource("img/home.jpg")), size=(1000, 600))
        bgImageLabel = ctk.CTkLabel(
            master=frameBody, text="Hola mundo nuevo", font=("Roboto", 50), image=bgImage)
        bgImageLabel.pack(expand=True, fill="both")

    def loadFooter(self):
        frameFooter = ctk.CTkFrame(
            master=self.container, height=100, width=1000, fg_color="blue")
        frameFooter.pack(side=ctk.BOTTOM, fill=ctk.X, padx=2, pady=2)
        label = ctk.CTkLabel(
            frameFooter, text="Foodie Tour es una marca registrada de Foodie Tour. All right reserved © 2023", text_color="white")
        label.pack(padx=10, pady=10)

    def signupView(self):
        pass

    def success(self):
        print("EXITO")
