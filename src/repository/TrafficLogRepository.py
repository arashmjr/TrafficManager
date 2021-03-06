from django.db.models.manager import Manager
from src.domain.models.TrafficLogDomainModel import TrafficLogDomainModel


class TrafficLogRepository:
    collection: Manager

    def __init__(self, collection: Manager):
        self.collection = collection

    def insert(self, model: TrafficLogDomainModel):
        result = self.collection.objects.create(**model.to_dict())
        return result

    def bulk_insert(self, models: [TrafficLogDomainModel]):
        dicts = map(lambda x: x.to_dict(), models)
        result = self.collection.bulk_create(dicts)

    def find_record_by_vehicle_type(self, vehicle_type: str):
        result = self.get_logs(vehicle_type=vehicle_type)
        return result

    def find_record_by_road_width(self, road_width: int):
        return self.get_logs(road_width=road_width)

    def get_logs(self, *args, **kwargs):
        return self.collection.objects.filter(*args, **kwargs)

    def remove_all(self):
        x = self.collection.objects.all()
        y =x.delete()
        return y
