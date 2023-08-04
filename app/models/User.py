class User:
    def __init__(self, id=None, history=[]):
        self.id = id
        self.history = history

    @classmethod
    def from_dict(cls, dictionary):
        return cls(
            dictionary.get('id', None),
            dictionary.get('history', [])
        )

    def to_dict(self):
        return {
            "id": self.id,
            "history": self.history
        }
