import abc
import importlib
import os
from config import PATH


class Controller(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def main(self):
        return

    def loadView(self, viewName):
        response = None
        if os.path.exists(f"{PATH}/views/{viewName}.py"):
            module = importlib.import_module(f"views.{viewName}")
            class_ = getattr(module, f"{viewName[0].upper()+viewName[1:]}View")
            response = class_(self)
        return response
