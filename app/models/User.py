class User:
    def __init__(self, id=None, history=[]):
        self.id = id
        self.history = history

    @classmethod
    def from_dict(cls, dictionary):
        return cls(dictionary)

    def to_dict(self):
        return {
            "id": self.id,
            "history": self.history
        }
