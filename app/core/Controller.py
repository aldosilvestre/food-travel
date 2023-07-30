import abc
import importlib
import os
from app.config import PATH


class Controller(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def main(self):
        return

    def loadView(self, view):
        response = None
        viewName = f"{view[0].upper()}{view[1::]}View"
        if os.path.exists(f"{PATH}/views/{viewName}.py"):
            module = importlib.import_module(f"views.{viewName}")
            class_ = getattr(module, f"{viewName}")
            response = class_(self)
        return response
