class RoadDomainModel:
    name: str
    origin: str
    destination: str
    minimum_height: float
    width: float
    geom: str

    def __init__(self, name: str, origin: str, destination: str, minimum_height: float, width: float, geom: str):

        self.name = name
        self.origin = origin
        self.destination = destination
        self.destination = destination
        self.minimum_height = minimum_height
        self.width = width
        self.geom = geom

    def to_dict(self):
        return {
                "name": self.name,
                "origin": self.origin,
                "destination": self.destination,
                "minimum_height": self.minimum_height,
                "width": self.width,
                "geom": self.geom

                }

