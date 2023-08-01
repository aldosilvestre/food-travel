from repositories.ubication import UbicationRepository


class UbicationService:

    def find_by_id(self, ubication_id):
        return UbicationRepository.find_by_id(ubication_id)

    def find_by_address(self, addr):
        return UbicationRepository.find_by_address(addr)


ubication_service = UbicationService()
