from repositories.activities import find_activity_by_id


class ActivityService:
    def get_activity_by_id(self, id):
        return find_activity_by_id(id)


activity_service = ActivityService()
