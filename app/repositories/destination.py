from db.connection import getConnection
from models.Destination import Destination
from core.Session import Session
import uuid


class DestinationRepository:

    @classmethod
    def find_all(cls):
        list_destinies = list(getConnection().Destination.find({'disponibility': {"$in": ['Si', 'SI', 'si']}}))
        return [Destination.from_dict(destiny) for destiny in list_destinies]

    @classmethod
    def save(cls, destination):
        destination.id = str(uuid.uuid4())
        result = getConnection().Destination.insert_one(destination.to_dict())
        return result

    @classmethod
    def find_by_id(cls, id):
        result = getConnection().Destination.find_one({'id': id})
        return Destination.from_dict(result)

    @classmethod
    def find_by_ubication(cls, ubication):
        return Destination.from_dict(getConnection().Destination.find_one({'ubication': ubication}))


destinies = [
    {
        "id": 1,
        "name": "Restaurante Italiano",
        "type": "Italiana",
        "ingredients": ["pasta", "tomate", "queso"],
        "min_price": 10.99,
        "max_price": 25.99,
        "popularity": 4.5,
        "disponibility": True,
        "ubication": 101,
        "image": "https://foodandpleasure.com/wp-content/uploads/2018/06/piantao-3.jpg"
    },
    {
        "id": 2,
        "name": "Restaurante Mediterráneo",
        "type": "Mediterránea",
        "ingredients": ["aceite de oliva", "pescado", "verduras"],
        "min_price": 12.50,
        "max_price": 30.00,
        "popularity": 4.0,
        "disponibility": False,
        "ubication": 102,
        "image": "https://i.pinimg.com/originals/1e/6b/65/1e6b656405c66fc6ed37891fb24766e5.jpg"
    },
    {
        "id": 3,
        "name": "Restaurante Regional",
        "type": "Regional",
        "ingredients": ["maíz", "carne de cerdo", "chiles"],
        "min_price": 8.99,
        "max_price": 20.00,
        "popularity": 4.8,
        "disponibility": True,
        "ubication": 103,
        "image": "https://www.lobostudio.es/wp-content/uploads/2020/10/3.IKIBANA-1536x1023.jpg"
    },
    {
        "id": 4,
        "name": "Restaurante Hindú",
        "type": "Hindú",
        "ingredients": ["curry", "arroz", "lentejas"],
        "min_price": 9.50,
        "max_price": 22.99,
        "popularity": 4.2,
        "disponibility": True,
        "ubication": 104,
        "image": "https://i.ytimg.com/vi/IF0VmMv2aFw/maxresdefault.jpg"
    },
    {
        "id": 5,
        "name": "Restaurante de Mariscos",
        "type": "Mariscos",
        "ingredients": ["camarones", "pulpo", "pescado"],
        "min_price": 15.99,
        "max_price": 35.99,
        "popularity": 4.6,
        "disponibility": True,
        "ubication": 105,
        "image": "https://www.momalia.com/wp-content/uploads/2019/09/decoracion-restaurantes-01.jpg"
    }
]
