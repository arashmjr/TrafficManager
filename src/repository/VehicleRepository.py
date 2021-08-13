from django.db.models.manager import Manager
from src.domain.models.VehicleDomainModel import VehicleDomainModel
from src.domain.entities.Driver import Driver


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

    # def join_three_table(self):
        # drivers = self.collection.objects.filter(Payment__status)
        # r =self.collection.objects.select_related(Payment.status)
        # r = self.collection.objects.filter(driver_id=self.collection.driver_id).select_related('Payment', 'Vehicle')

        # print(type(Payment))
        # r = self.collection.objects.filter(Driver__driver_id__Payment__status='notpaid')
        # print(r)

        # self.collection.objects.filter(entry__headline__contains='Lennon').filter(entry__pub_date__year=2008)

        # print(self.collection.objects.select_related('owner_id'))







