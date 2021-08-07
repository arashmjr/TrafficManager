from django.db.models.manager import Manager
from src.domain.models.VehicleDomainModel import VehicleDomainModel


class VehicleRepository:
    collection: Manager

    def __init__(self, collection: Manager):
        self.collection = collection

    def insert(self, model: VehicleDomainModel):
        result = self.collection.objects.create(**model.to_dict())
        return result

    def find_record_by_color(self, color: str):
        return self.collection.objects.filter(color=color)
