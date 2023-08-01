from repositories.destination import DestinationRepository
from models.Destination import Destination
from dto.DestinationDto import DestinationDto
from services.ubication_service import ubication_service


class DestinationService:

    def find_all(self) -> [DestinationDto]:
        result = []
        destinations = DestinationRepository.find_all()
        for destiny in destinations:
            ubication = ubication_service.find_by_id(destiny.ubication)
            result.append(DestinationDto(destiny, ubication))
        return result

    def save(self, destination):
        return DestinationRepository.save(destination)

    def delete(self, destination):
        print("Deleting destination")

    def update(self, id, destination):
        print("Updating destination")

    def get_destiny_by_id(self, destiny_id) -> Destination:
        return DestinationRepository.find_by_id(destiny_id)

    def find_by_address(self, addr):
        result = []
        ubications = ubication_service.find_by_address(addr)
        for ubication in ubications:
            destiny = DestinationRepository.find_by_ubication(ubication.id)
            result.append(DestinationDto(destiny, ubication))
        return result


destination_service = DestinationService()
