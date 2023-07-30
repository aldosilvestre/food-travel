import os
import importlib
from config import PATH


class Core:
    @staticmethod
    def openController(controller):
        response = None

        controllerName = f"{controller[0].upper()}{controller[1:]}Controller"

        if os.path.exists(f"{PATH}/controllers/{controllerName}.py"):
            module = importlib.import_module("controllers." + controllerName)
            class_ = getattr(module, controllerName)
            response = class_()
        return response

    @staticmethod
    def openComponent(component, container, last_frame=None):
        response = None

        componentName = f"{component[0].upper()}{component[1:]}Component"

        if os.path.exists(f"{PATH}/views/components/{componentName}.py"):
            module = importlib.import_module("app.views.components." + componentName)
            class_ = getattr(module, componentName)
            response = class_(container, last_frame)
        return response
