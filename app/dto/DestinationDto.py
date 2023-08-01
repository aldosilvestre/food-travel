
class DestinationDto:
    def __init__(self, destination, ubication):
        self.id = destination.id
        self.name = destination.name
        self.type = destination.type
        self.ingredients = destination.ingredients
        self.min_price = destination.min_price
        self.max_price = destination.max_price
        self.popularity = destination.popularity
        self.disponibility = destination.disponibility
        self.ubication = ubication
        self.image = destination.image