from src.domain.entities.Vehicle import Vehicle
from src.domain.entities.Road import Road
import datetime


class TrafficLogDomainModel:
    road_id: int
    vehicle_id: int
    vehicle_type: str
    vehicle_color: str
    road_width: int
    date: datetime
    province_name: str
    latitude: float
    longitude: float

    def __init__(self, road_id: int, vehicle_id: int, vehicle_type: str, vehicle_color: str, road_width: int,
                 date: datetime, province_name: str, latitude: float, longitude: float):

        self.road_id = road_id
        self.vehicle_id = vehicle_id
        self.vehicle_type = vehicle_type
        self.vehicle_color = vehicle_color
        self.road_width = road_width
        self.date = date
        self.province_name = province_name
        self.latitude = latitude
        self.longitude = longitude

    def to_dict(self):

        converted_dict = {
                "road_id": Road(self.road_id) if self.road_id is not None else None,
                "vehicle_id": Vehicle(self.vehicle_id) if self.vehicle_id is not None else None,
                "vehicle_type": self.vehicle_type,
                "vehicle_color": self.vehicle_color,
                "road_width": self.road_width,
                "date": self.date,
                "province_name": self.province_name,
                "latitude": self.latitude,
                "longitude": self.longitude
                }

        return converted_dict

    @staticmethod
    def asJSON(logs):
        list_logs = []
        for item in logs:
            result = {

                'road_id': item.road_id.road_id,
                'vehicle_id': item.vehicle_id.vehicle_id,
                'vehicle_type': item.vehicle_type,
                'vehicle_color': item.vehicle_color,
                'road_width': item.road_width,
                'date': item.date,
                'province_name': item.province_name,
                'latitude': item.latitude,
                'longitude': item.longitude
            }
            list_logs.append(result)
        return list_logs
