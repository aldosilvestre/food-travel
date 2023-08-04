from services.tour_service import tour_service


class TourController:

    def get_tour(self):
        return tour_service.get_tour()


    def subscribe_to_tour(self, activity):
        return tour_service.subscribe_to_tour(activity)


tour_controller = TourController()