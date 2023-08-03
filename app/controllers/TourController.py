from services.tour_service import tour_service


class TourController:

    def get_tour(self):
        return tour_service.get_tour()
