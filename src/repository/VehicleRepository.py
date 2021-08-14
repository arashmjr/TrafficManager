from django.db.models.manager import Manager
from src.domain.models.VehicleDomainModel import VehicleDomainModel


class VehicleRepository:
    collection: Manager

    def __init__(self, collection: Manager):
        self.collection = collection

    def insert(self, model: VehicleDomainModel):
        result = self.collection.objects.create(**model.to_dict())
        return result

    def find_record_by_colors(self, colors):
        return self.collection.objects.filter(color__in=colors)

    def find_record_by_owner_id(self, owner_id: int):
        return self.collection.objects.filter(owner_id=owner_id)

    def find_record_by_list_owner_id(self, array: list):
        list_vehicles = []
        for item in array:
            records = self.collection.objects.filter(owner_id=item['driver_id'])
            for segment in records:
                list_vehicles.append(segment)

        return list_vehicles

    def get_vehicle_by(self, vehicle_ids):
        return self.collection.objects.filter(vehicle_id__in=vehicle_ids)

    def find_record_by_national_code(self, national_code):
        return self.collection.objects.get(national_code)









