from src.repository.VehicleRepository import VehicleRepository
from src.repository.TrafficLogRepository import TrafficLogRepository
from src.domain.models.TrafficLogDomainModel import TrafficLogDomainModel
from django.core.handlers.wsgi import WSGIRequest
from itertools import chain
import datetime


class TrafficLogService:
    repository_log: TrafficLogRepository

    def __init__(self, repository_log: TrafficLogRepository):
        self.repository_log = repository_log

    def add_traffic_log(self, json: str):

        date = datetime.datetime.now()
        model = TrafficLogDomainModel(json['road_id'], json['vehicle_id'], json['vehicle_type'],
                                      json['vehicle_color'], json['road_width'], date,
                                      json['province_name'], json['latitude'], json['longitude'])

        self.repository_log.insert(model)
        return True



