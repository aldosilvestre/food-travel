import os

global PATH
PATH = os.path.dirname(os.path.realpath(__file__))


def get_resource(name):
    return os.path.join(PATH, "resources", name)


global CONFIG
CONFIG = {
    "font-header": "Roboto Condensed",
    "font-family": "Open Sans",
    "color-primary": "#FF5722",
    "color-secondary": "#607D8B",
    "color-btn": "#4CAF50",
    "color-background": "#EEEEEE"
}
