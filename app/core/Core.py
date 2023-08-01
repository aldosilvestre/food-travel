import os
import importlib
from config import PATH


class Core:
    @staticmethod
    def open_controller(controller):
        response = None

        controller_name = f"{controller[0].upper()}{controller[1:]}Controller"

        if os.path.exists(f"{PATH}/controllers/{controller_name}.py"):
            module = importlib.import_module("controllers." + controller_name)
            class_ = getattr(module, controller_name)
            response = class_()
        return response

    @staticmethod
    def open_component(component, container, last_frame=None):
        response = None

        component_name = f"{component[0].upper()}{component[1:]}Component"

        if os.path.exists(f"{PATH}/views/components/{component_name}.py"):
            module = importlib.import_module("views.components." + component_name)
            class_ = getattr(module, component_name)
            response = class_(container, last_frame)
        return response
