from services.activities_service import activity_service
from models.Activity import Activity
class ActivityController:

    def new_destiny(self, **kwargs):
        new_destination = Destination(dict(kwargs))
        destination_service.save(new_destination)

    def new_activity(self, **kwargs):
        new_activity = Activity(dict(kwargs))
        return activity_service.save(new_activity)

    def get_destiny_by_id(self, id):
        return destination_service.get_destiny_by_id(id)

    def get_all(self):
        return activity_service.find_all()

    def get_by_address(self, addr):
        return activity_service.find_by_address(addr)


activity_controller = ActivityController()
