class RoadDomainModel:
    name: str
    origin: str
    destination: str
    minimum_height: float
    width: float

    def __init__(self, name: str, origin: str, destination: str, minimum_height: float, width: float):

        self.name = name
        self.origin = origin
        self.destination = destination
        self.destination = destination
        self.minimum_height = minimum_height
        self.width = width

    def to_dict(self):
        return {
                "name": self.name,
                "origin": self.origin,
                "destination": self.destination,
                "minimum_height": self.minimum_height,
                "width": self.width

                }
