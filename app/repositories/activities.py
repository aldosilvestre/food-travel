from models.Activity import Activity
import datetime
from db.connection import getConnection
import uuid
from models.Activity import Activity
from datetime import datetime


class ActivityRepository:

    @staticmethod
    def save(activity):
        activity.id = str(uuid.uuid4())
        return getConnection().Activity.insert_one(activity.to_dict())

    @staticmethod
    def find_all():
        activities = list(getConnection().Activity.find({"datetime": {"$gt": datetime.now()}}))
        return [Activity.from_dict(activity) for activity in activities]

    @staticmethod
    def find_activities_by_user(user_id) -> [Activity]:
        return activities

    @staticmethod
    def find_by_destiny(destiny_id) -> Activity:
        return Activity.from_dict(getConnection().Activity.find_one({'destiny_id': destiny_id}))

    @staticmethod
    def find_activity_by_id(activity_id) -> Activity:
        result = []
        for activity in activities:
            result.append(Activity.from_dict(activity))
        return next(filter(lambda element: element.id == activity_id, result), None)

    @staticmethod
    def get_activities_by_ids(list_id) -> [Activity]:
        result = []
        for activity in activities:
            if activity.id in list_id:
                result.append(Activity.from_dict(activity))
        return result


activities = [
    {
        "id": 1,
        "name": "Degustación de vinos",
        "destiny_id": 1,
        "datetime": "2023-07-04T09:00:00"
    },
    {
        "id": 2,
        "name": "Espectáculo de música en vivo",
        "destiny_id": 3,
        "datetime": "2023-07-04T15:30:00"
    },
    {
        "id": 3,
        "name": "Clase de cocina italiana",
        "destiny_id": 2,
        "datetime": "2023-07-05T11:00:00"
    }
]
