import tkinter as tk
from views.components.NewDestinyComponent import NewDestinyComponent


class Operations:
    @staticmethod
    def create_destiny():
        toplevel = tk.Toplevel()
        toplevel.lift()
        toplevel.focus_force()
        NewDestinyComponent(toplevel)

    def create_admin_user(self):
        pass


operations = Operations()
