from views.view import View
import customtkinter as ctk


class LoginView(ctk.CTk, View):

    def __init__(self, controller):
        super().__init__()
        self.title("Login")
        self.login = controller

        frame = ctk.CTkFrame(master=self).grid()
        self.button = ctk.CTkButton(
            frame, text="Iniciar Sesion", command=(self.loginButtonEvent))
        self.button.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

    def loginButtonEvent(self):
        result = self.login.signIn("aldo", "password")
        if result:
            print("todo ok")
        else:
            label = ctk.CTkLabel(
                master=self, text="fallo el inicio de sesion", text_color="red")
            label.place(relx=0.5, rely=0.7, anchor=ctk.CENTER)
            self.close()

    def main(self):
        self.mainloop()

    def close(self):
        return
