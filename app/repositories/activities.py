from models.Activity import Activity
import datetime


def find_activities_by_user(user_id) -> [Activity]:
    return activities


def find_activity_by_id(activity_id) -> Activity:
    result = []
    for activity in activities:
        result.append(Activity.from_dict(activity))
    return next(filter(lambda element: element.id == activity_id, result), None)


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
