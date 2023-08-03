from repositories.ubication import UbicationRepository


class UbicationService:

    def save(self, new_ubication):
        return UbicationRepository.save(new_ubication)

    def find_by_id(self, ubication_id):
        return UbicationRepository.find_by_id(ubication_id)

    def find_by_address(self, addr):
        return UbicationRepository.find_by_address(addr)

    def new_center(self, latitude, longitude):
        print(latitude)
        print(longitude)
        pass


ubication_service = UbicationService()
