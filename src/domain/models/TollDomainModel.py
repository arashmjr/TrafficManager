from src.domain.entities.Road import Road


class TollDomainModel:
    road_id: int
    name: str
    heavy_vehicle_charge: int
    light_vehicle_charge: int
    heavy_vehicle_charge_per_kg: int
    latitude: float
    longitude: float

    def __init__(self, road_id: int, name: str, heavy_vehicle_charge: int, light_vehicle_charge: int,
                 heavy_vehicle_charge_per_kg: int, latitude: float, longitude: float):

        self.road_id = road_id
        self.name = name
        self.heavy_vehicle_charge = heavy_vehicle_charge
        self.light_vehicle_charge = light_vehicle_charge
        self.heavy_vehicle_charge_per_kg = heavy_vehicle_charge_per_kg
        self.latitude = latitude
        self.longitude = longitude

    def to_dict(self):
        return {
                "road_id": Road(self.road_id) if self.road_id is not None else None,
                "name": self.name,
                "heavy_vehicle_charge": self.heavy_vehicle_charge,
                "light_vehicle_charge": self.light_vehicle_charge,
                "heavy_vehicle_charge_per_kg": self.heavy_vehicle_charge_per_kg,
                "latitude": self.latitude,
                "longitude": self.longitude

                }

    @staticmethod
    def asJSON(station_tolls):
        list_station_tolls = []
        for item in station_tolls:
            result = {

                'road_id': item.road_id.road_id,
                'name': item.name,
                'heavy_vehicle_charge': item.heavy_vehicle_charge,
                'light_vehicle_charge': item.light_vehicle_charge,
                'heavy_vehicle_charge_per_kg': item.heavy_vehicle_charge_per_kg,
                'latitude': item.latitude,
                'longitude': item.longitude
            }
            list_station_tolls.append(result)
        return list_station_tolls
