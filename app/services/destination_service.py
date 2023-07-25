from repository.destination import DestinationRepository


def save(destination):
    return DestinationRepository.save(destination)


def delete(destination):
    print("Deleting destination")


def update(id, destination):
    print("Updating destination")
