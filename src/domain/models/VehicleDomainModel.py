from src.domain.entities.Driver import Driver


class VehicleDomainModel:
    plate_number: int
    national_code: int
    color: str
    type: str
    weight: int
    height: int
    model: str
    year: int

    def __init__(self, plate_number, national_code: int, color: str, type: str, weight: int, height: int, model: str, year: int):

        self.plate_number = plate_number
        self.national_code = national_code
        self.color = color
        self.type = type
        self.weight = weight
        self.height = height
        self.model = model
        self.year = year

    def to_dict(self):
        return {
                "plate_number": self.plate_number,
                "national_code": Driver(self.national_code),
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
                'plate_number': item.plate_number,
                'national_code': item.national_code.national_code,
                'color': item.color,
                'type': item.type,
                'weight': item.weight,
                'height': item.height,
                'model': item.model,
                'year': item.year
            }
            list_vehicles.append(result)
        return list_vehicles
