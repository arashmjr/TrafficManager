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

    def find_record_by_owner_id(self, owner_id: int):
        return self.collection.objects.filter(owner_id=owner_id)

    def find_record_by_list_owner_id(self, array: list):
        list_vehicles = []
        for item in array:
            records = self.collection.objects.filter(owner_id=item['driver_id'])
            for segment in records:
                list_vehicles.append(segment)

        return list_vehicles







