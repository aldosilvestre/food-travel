from db.connection import getConnection
from models.Ubication import Ubication
import uuid
import re


def have_string(address, text_search):
    return text_search.lower() in address.lower()


class UbicationRepository:

    @staticmethod
    def save(ubication):
        ubication.id = str(uuid.uuid4())
        getConnection().Ubication.insert_one(ubication.to_dict())
        return ubication.id

    @staticmethod
    def find_by_id(ubication_id):
        return Ubication.from_dict(getConnection().Ubication.find_one({"id": ubication_id}))

    @staticmethod
    def find_by_address(addr):
        result = getConnection().Ubication.find(
            {"address": {"$regex": re.escape(addr), "$options": "i"}})
        return [Ubication.from_dict(ubication) for ubication in result]



ubications = [
    {
        "id": 101,
        "address": "Tour Gastronómico 101",
        "coordinates": [-24.79751134026236, -65.4112654796014],
    }, {
        "id": 102,
        "address": "Tour Gastronómico 102",
        "coordinates": [-24.799157307558, -65.4164045683142],
    }, {
        "id": 103,
        "address": "Tour Gastronómico 103",
        "coordinates": [-24.803666574186288, -65.40584737008436],
    }, {
        "id": 104,
        "address": "Tour Gastronómico 104",
        "coordinates": [-24.809052222554453, -65.40965616655065],
    }, {
        "id": 105,
        "address": "Tour Gastronómico 105",
        "coordinates": [-24.799834464609365, -65.42019831387337],
    }, {
        "id": 106,
        "address": "Tour Gastronómico 106",
        "coordinates": [-24.79346436220292, -65.41155150105791],
    },

]
