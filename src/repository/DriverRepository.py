from django.db.models.manager import Manager
from src.domain.models.DriverDomainModel import DriverDomainModel


class DriverRepository:
    collection: Manager

    def __init__(self, collection: Manager):
        self.collection = collection

    def insert(self, model: DriverDomainModel):
        result = self.collection.objects.create(**model.to_dict())
        return result

    def get_owners_by(self, owner_ids):
        return self.collection.objects.filter(driver_id__in=owner_ids)

    def find_record_by_national_code(self, national_code):
        return self.collection.objects.get(national_code=national_code)

    def get_all(self):
        arr = []
        for x in self.collection.objects.filter():
            arr.append(x)
        return arr


