from services.destination_service import destination_service
from core.Session import Session
from services.activities_service import activity_service
from dto.TourDto import TourDto
from dto.ActivityDto import ActivityDto
from dto.DestinationDto import DestinationDto
from services.ubication_service import ubication_service
from repositories.tour import TourRepository

class TourService:
    def find_destinies(self):
        return destination_service.find_all()

    def get_tour(self):
        user = Session().get_session()
        tour =TourRepository.find_tour_by_user(user.id)
        activities = []

        for activity_id in tour.destinies:
            activity = activity_service.get_by_id(activity_id)
            destiny = destination_service.get_destiny_by_id(activity.destiny_id)
            destiny_dto = DestinationDto(destiny, destiny.ubication)
            activity_dto = ActivityDto(activity.id, activity.name, destiny_dto, activity.datetime)
            activities.append(activity_dto)
        return TourDto(tour, activities)

    def subscribe_to_tour(self, activity):
        user = Session().get_session()
        tour = TourRepository.find_tour_by_user(user.id)
        tour.destinies.append(activity.id)
        if tour.id is None:
            tour.user_id = user.id
            TourRepository.save(tour)
        else:
            TourRepository.update(tour)




    # def subscribse_to_tour(self, activity):
    #     user = Session().get_session()
    #     userdb = UserRepository.find_by_id(user.id)
    #     userdb.history.append(activity.id)
    #     if userdb.id is None:
    #         userdb.id = user.id
    #         UserRepository.save_new_user(userdb)
    #     else:
    #         UserRepository.update_user(userdb)


tour_service = TourService()
