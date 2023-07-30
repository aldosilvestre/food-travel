import customtkinter as ctk
from tkinter.font import BOLD


class SignupView:
    font = ("Roboto", 15, BOLD)

    fields = [
        ("name", "Nombre"),
        ("lastname", "Apellido"),
        ("age", "Edad"), ("username", "Nombre Usuario"),
        ("password", "Contraseña"),
        ("repeat_password", "Repetir Contraseña")]

    def __init__(self, root):
        self.root = root
        self.login = ctk.CTkToplevel(master=root)
        self.login.title("Registrarse")
        self.login.resizable(False, False)
        self.login.geometry("500x550")
        self.form = []

        frame = ctk.CTkFrame(self.login)
        frame.pack(padx=10, pady=10, ipadx=10, ipady=10, anchor=ctk.CENTER)

        self.error_label = ctk.CTkLabel(frame, text="", text_color="red")
        self.error_label.grid(row=0, column=0, columnspan=2)

        indice = 2

        for field in self.fields:
            subframe = ctk.CTkFrame(frame, fg_color="transparent")
            subframe.grid(row=indice // 2, column=indice % 2, padx=20, pady=20, ipadx=20, ipady=20)
            label = ctk.CTkLabel(subframe, text=(field[1]), font=self.font, anchor='w')
            label.pack(pady=0, anchor=ctk.CENTER, fill="both")
            entry = ctk.CTkEntry(subframe)
            entry.pack(pady=5, anchor=ctk.CENTER, fill="both")
            if field[0] in ["password", "repeat_password"]:
                entry.configure(show="*")
            self.form.append({
                field[0]: entry})
            indice += 1

        login_button = ctk.CTkButton(
            frame, text="Registrarse", command=self.do_signup)
        # login_button.pack(pady=20, anchor=ctk.CENTER)
        login_button.grid(row=indice, column=0, columnspan=2)



    def do_signup(self):
        self.show_error_message("Ocurrio un error")
        pass

    def show_error_message(self, message):
        self.error_label.configure(text=message)
