from services.destination_service import destination_service
from models.Destination import Destination


class DestinationController:

    def new_destiny(self, **kwargs):
        new_destination = Destination(dict(kwargs))
        destination_service.save(new_destination)

    def get_destiny_by_id(self, id):
        return destination_service.get_destiny_by_id(id)

    def get_all(self):
        return destination_service.find_all()

    def get_by_address(self, addr):
        return destination_service.find_by_address(addr)


destination_controller = DestinationController()
