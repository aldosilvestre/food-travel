class Destination:

    def __init__(self, id="", name="", type="", ingredients=[], min_price=0, max_price=0, popularity=0, disponibility=0, ubication="", image=""):
        self.id = id
        self.name = name
        self.type = type
        self.ingredients = ingredients
        self.min_price = min_price
        self.max_price = max_price
        self.popularity = popularity
        self.disponibility = disponibility
        self.ubication = ubication
        self.image = image

    @classmethod
    def from_dict(cls, destionation):
        return cls(
            destionation['id'],
            destionation['name'],
            destionation['type'],
            destionation['ingredients'],
            destionation['min_price'],
            destionation['max_price'],
            destionation['popularity'],
            destionation['disponibility'],
            destionation['ubication'],
            destionation['image']
        )

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "type": self.type,
            "ingredients": self.ingredients,
            "min_price": self.min_price,
            "max_price": self.max_price,
            "popularity": self.popularity,
            "disponibility": self.disponibility,
            "ubication": self.ubication,
            "image": self.image
        }
