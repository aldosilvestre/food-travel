class Tour:
    def __init__(self, id=None, name="", destinies=[]):
        self.id = id
        self.name = name
        self.destinies = destinies

    @classmethod
    def from_dict(cls, tour):
        return cls(
            tour['id'],
            tour['name'],
            tour['destinies'],
        )

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "destinies": self.destinies
        }
