from services.ubication_service import ubication_service

class UbicationController:

    def new_center(self, latitude, longitude):
        return ubication_service.new_center(latitude, longitude)



ubication_controller = UbicationController()
