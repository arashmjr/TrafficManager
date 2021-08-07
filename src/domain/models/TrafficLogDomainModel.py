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
        return {
                "road_id": self.road_id,
                "vehicle_id": self.vehicle_id,
                "vehicle_type": self.vehicle_type,
                "vehicle_color": self.vehicle_color,
                "road_width": self.road_width,
                "date": self.date,
                "province_name": self.province_name,
                "latitude": self.latitude,
                "longitude": self.longitude

                }
