class Ubication:
    def __init__(self, id=None, address="", coordenates=""):
        self.id = id
        self.address = address
        self.coordinates = coordenates

    @classmethod
    def from_dict(cls, ubication):
        return cls(
            ubication['id'],
            ubication['address'],
            ubication['coordinates'],
        )

    def to_dict(self):
        return {
            "id": self.id,
            "address": self.name,
            "coordinates": self.coordinates
        }
