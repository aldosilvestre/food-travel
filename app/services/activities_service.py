from repositories.activities import ActivityRepository
from services.destination_service import destination_service
from dto.ActivityDto import ActivityDto
from services.destination_service import destination_service


class ActivityService:

    def save(self, activity):
        return ActivityRepository.save(activity)

    def find_all(self):
        result = []
        activities = ActivityRepository.find_all()
        for activity in activities:
            destiny = destination_service.get_destiny_by_id(activity.destiny_id)
            result.append(ActivityDto(activity.id, activity.name, destiny, activity.datetime))
        return result

    def get_by_destiny(self, destiny_id):
        return ActivityRepository.find_by_destiny(destiny_id)

    def get_by_id(self, activity_id):
        return ActivityRepository.find_activity_by_id(activity_id)

    def find_by_address(self, addr):
        result = []
        destinies = destination_service.find_by_address(addr)
        for destiny in destinies:
            activity = activity_service.get_by_destiny(destiny.id)
            result.append(ActivityDto(activity.id, activity.name, destiny, activity.datetime))
        return result

activity_service = ActivityService()
