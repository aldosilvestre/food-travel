from models.Tour import Tour
import datetime


def find_tour_from_user(user_id):
    return Tour() # Tour.from_dict(tour)


tour = {
    "id": 1,
    "name": "Tour Gastronómico",
    "destinies": [1, 2, 3],
}
