class Activity:
    def __init__(self, id=None, name="", destiny_id=None, datetime=""):
        self.id = id
        self.name = name
        self.destiny_id = destiny_id
        self.datetime = datetime

    @classmethod
    def from_dict(cls, activity):
        return cls(
            activity['id'],
            activity['name'],
            activity['destiny_id'],
            activity['datetime']
        )

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "destiny_id": self.destiny_id,
            "datetime": self.datetime,
        }
