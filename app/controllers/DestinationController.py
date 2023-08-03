from services.destination_service import destination_service
from models.Destination import Destination
from models.Ubication import Ubication


class DestinationController:

    def new_destiny(self, dictionary):
        new_destination = Destination(dictionary)
        new_destination.ingredients = dictionary['ingredients'].split(',')
        new_ubication = Ubication(address=dictionary['address'],
                                              coordenates=[dictionary['ubication_latitude'],
                                                           dictionary['ubication_longitude']])
        destination_service.save(new_destination, new_ubication)

    def get_destiny_by_id(self, id):
        return destination_service.get_destiny_by_id(id)

    def get_all(self):
        return destination_service.find_all()

    def get_by_address(self, addr):
        return destination_service.find_by_address(addr)


destination_controller = DestinationController()
