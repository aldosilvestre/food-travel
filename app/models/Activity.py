class Activity:
    def __init__(self, dictionary: object = {}):
        self.id = dictionary.get('id', "")
        self.name = dictionary.get('name', "")
        self.destiny_id = dictionary.get('destiny_id', '')
        self.datetime = dictionary.get('datetime', '')

    @classmethod
    def from_dict(cls, activity):
        return cls(activity)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "destiny_id": self.destiny_id,
            "datetime": self.datetime,
        }
