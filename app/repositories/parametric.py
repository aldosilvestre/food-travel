from db.connection import getConnection
from models.Parametric import Parametric


class ParametricRepository:

    @staticmethod
    def find_by_key(key):
        return Parametric.from_dict(getConnection().Parametric.find_one({"key": key}))
