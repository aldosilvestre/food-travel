from app.services.plain_service import find_destinies


class PlainController:
    def __init__(self):
        pass

    def getDestinies(self):
        return [destiny.to_dict() for destiny in find_destinies()]
