import tkinter as tk
import os
import importlib
from config import PATH


class Operations:

    def go_to(self, component):
        toplevel = tk.Toplevel()
        toplevel.resizable(False, False)
        toplevel.lift()
        toplevel.focus_force()

        if os.path.exists(f"{PATH}/views/components/{component}.py"):
            module = importlib.import_module(f"views.components.{component}")
            class_ = getattr(module, f"{component}")
            class_(toplevel)


operations = Operations()
