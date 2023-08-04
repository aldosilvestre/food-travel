from models.Tour import Tour
import datetime
from db.connection import getConnection
from models.Tour import Tour
import uuid

class TourRepository:

    @staticmethod
    def find_tour_by_user(user_id):
        tour = getConnection().Tour.find_one({'user_id': user_id})
        if tour is None:
            return Tour()
        else:
            return Tour.from_dict(tour)

    @staticmethod
    def save(tour):
        tour.id = str(uuid.uuid4())
        return getConnection().Tour.insert_one(tour.to_dict())

    @staticmethod
    def update(tour):
        return getConnection().Tour.update_one({'user_id': tour.user_id}, {'$set': {"destinies": tour.destinies}})


tour = {
    "id": 1,
    "name": "Tour Gastronómico",
    "destinies": [1, 2, 3],
}
