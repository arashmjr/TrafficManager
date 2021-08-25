from django.db.models.manager import Manager
from src.domain.models.VehicleDomainModel import VehicleDomainModel


class VehicleRepository:
    collection: Manager

    def __init__(self, collection: Manager):
        self.collection = collection

    def insert(self, model: VehicleDomainModel):
        print(model.to_dict())
        result = self.collection.objects.create(**model.to_dict())
        return result

    def find_record_by_colors(self, colors):
        return self.collection.objects.filter(color__in=colors)

    def find_record_by_list_national_code(self, array: list):
        list_vehicles = []
        for item in array:
            records = self.collection.objects.filter(national_code=item['national_code'])
            for segment in records:
                list_vehicles.append(segment)

        return list_vehicles

    def get_vehicle_by(self, vehicle_ids):
        return self.collection.objects.filter(vehicle_id__in=vehicle_ids)

    def find_record_by_national_code(self, national_code: int):
        return self.collection.objects.filter(national_code=national_code)

    def remove_all(self):
        x = self.collection.objects.all()
        y =x.delete()
        return y











