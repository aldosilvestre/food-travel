from db.connection import getConnection


class DestinationRepository:
    @classmethod
    def save(cls, destination):
        db = getConnection()
        result = db.Destination.insert_one(destination.to_dict())
        return result
