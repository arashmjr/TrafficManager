from src.domain.entities.Driver import Driver


class VehicleDomainModel:
    owner_id: int
    color: str
    type: str
    weight: int
    height: int
    model: str
    year: int

    def __init__(self, owner_id: int, color: str, type: str, weight: int, height: int, model: str, year: int):

        self.owner_id = owner_id
        self.color = color
        self.type = type
        self.weight = weight
        self.height = height
        self.model = model
        self.year = year

    def to_dict(self):
        return {
                "owner_id": Driver(self.owner_id),
                "color": self.color,
                "type": self.type,
                "weight": self.weight,
                "height": self.height,
                "model": self.model,
                "year": self.year

                }

    @staticmethod
    def asJSON(vehicles):
        list_vehicles = []
        for item in vehicles:

            result = {

                'owner_id': item.owner_id.driver_id,
                'color': item.color,
                'type': item.type,
                'weight': item.weight,
                'height': item.height,
                'model': item.model,
                'year': item.year
            }
            list_vehicles.append(result)
        return list_vehicles
