import os
import importlib
from config import PATH


class Core:
    @staticmethod
    def openController(controller):
        response = None

        controller = controller[0].upper()+controller[1:]
        controllerName = controller+"Controller"

        if os.path.exists(f"{PATH}/controllers/{controllerName}.py"):
            module = importlib.import_module("controllers."+controllerName)
            class_ = getattr(module, controllerName)
            response = class_()
        return response
