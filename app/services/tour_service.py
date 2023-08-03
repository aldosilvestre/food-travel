from services.destination_service import destination_service
from core.Session import Session
from repositories.tour import find_tour_from_user
from services.activities_service import activity_service
from dto.TourDto import TourDto
from dto.ActivityDto import ActivityDto
from dto.DestinationDto import DestinationDto
from services.ubication_service import ubication_service


class TourService:
    def find_destinies(self):
        return destination_service.find_all()

    def get_tour(self):
        user = Session().get_session()
        tour = find_tour_from_user(user.id)
        activities = []

        for activity_id in tour.destinies:
            activity = activity_service.get_by_id(activity_id)
            destiny = destination_service.get_destiny_by_id(activity.destiny_id)

            destiny_dto = DestinationDto(destiny, destiny.ubication)
            activity_dto = ActivityDto(activity.id, activity.name, destiny_dto, activity.datetime)
            activities.append(activity_dto)
        return TourDto(tour, activities)


tour_service = TourService()
