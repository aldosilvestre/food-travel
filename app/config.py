import os

global PATH
PATH = os.path.dirname(os.path.realpath(__file__))


def getResource(name):
    return os.path.join(PATH, "resources", name)
