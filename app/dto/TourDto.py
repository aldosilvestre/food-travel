class TourDto:
    def __init__(self, tour, activities):
        self.id = tour.id
        self.name = tour.name
        self.activities = activities
