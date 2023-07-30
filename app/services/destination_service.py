from app.repositories.destination import DestinationRepository
from app.models.Destination import Destination


def find_all() -> [Destination]:
    return DestinationRepository.find_all()


def save(destination):
    return DestinationRepository.save(destination)


def delete(destination):
    print("Deleting destination")


def update(id, destination):
    print("Updating destination")
