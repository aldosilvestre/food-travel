from app.services.destination_service import save
from app.models.Destination import Destination


class DestinationController:
    def __init__(self):
        pass

    def new_destiny(self, **kwargs):
        new_destination = Destination(dict(kwargs))
        save(new_destination)
