from django.db.models.manager import Manager
from src.domain.models.TrafficLogDomainModel import TrafficLogDomainModel


class TrafficLogRepository:
    collection: Manager

    def __init__(self, collection: Manager):
        self.collection = collection

    def insert(self, model: TrafficLogDomainModel):
        result = self.collection.objects.create(**model.to_dict())
        return result

    def find_record_by_vehicle_type(self, vehicle_type: str):
        result = self.collection.objects.filter(vehicle_type=vehicle_type)
        return result

    def find_record_by_road_width(self, road_width: int):
        result = self.collection.objects.filter(road_width=road_width)
        return result

