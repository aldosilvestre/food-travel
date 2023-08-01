import abc
import importlib
import os
from config import PATH


class Controller(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def main(self):
        return

    def load_view(self, view):
        response = None
        view_name = f"{view[0].upper()}{view[1::]}View"
        if os.path.exists(f"{PATH}/views/{view_name}.py"):
            module = importlib.import_module(f"views.{view_name}")
            class_ = getattr(module, f"{view_name}")
            response = class_(self)
        return response
