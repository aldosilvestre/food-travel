class Parametric:
    def __init__(self, dictionary: object = {}):
        self.key = dictionary.get('key', '')
        self.value = dictionary.get('value', {})

    @classmethod
    def from_dict(cls, dictionary):
        return cls(dictionary)

    def to_dict(self):
        return {
            "key": self.key,
            "value": self.value
        }
