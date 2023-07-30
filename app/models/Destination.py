class Destination:

    def __init__(self, dictionary: object = {}):
        self.id = dictionary.get('id', '')
        self.name = dictionary.get('name', '')
        self.type = dictionary.get('type', '')
        self.ingredients = dictionary.get('ingredients', [])
        self.min_price = dictionary.get('min_price', 0)
        self.max_price = dictionary.get('max_price', 0)
        self.popularity = dictionary.get('popularity', 0)
        self.disponibility = dictionary.get('disponibility', 0)
        self.ubication = dictionary.get('ubication', '')
        self.image = dictionary.get('image', '')

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
