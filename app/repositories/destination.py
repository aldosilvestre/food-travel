# from db.connection import getConnection
from app.models.Destination import Destination
from app.core.Session import Session

class DestinationRepository:

    @classmethod
    def find_all(cls):
        destiny = Destination()
        return [destiny]

    @classmethod
    def save(cls, destination):
        session = Session().get_session()
        print(f"El usuario {session.username} quizo guardar")
        print(destination)
        # db = getConnection()
        # result = db.Destination.insert_one(destination.to_dict())
        # return result
