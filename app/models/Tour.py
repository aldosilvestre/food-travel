class Tour:
    def __init__(self, id=None, name="", user_id=None, destinies=[]):
        self.id = id
        self.name = name
        self.user_id = user_id
        self.destinies = destinies

    @classmethod
    def from_dict(cls, tour):
        return cls(
            tour.get('id', None),
            tour.get('name', ''),
            tour.get('user_id', None),
            tour.get('destinies',[])
        )

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "user_id": self.user_id,
            "destinies": self.destinies
        }
