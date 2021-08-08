from django.db.models.manager import Manager
from src.domain.models.PaymentDomainModel import PaymentDomainModel


class PaymentRepository:
    collection: Manager

    def __init__(self, collection: Manager):
        self.collection = collection

    def insert(self, model: PaymentDomainModel):
        result = self.collection.objects.create(**model.to_dict())
        return result

    def find_record_by_date_range(self, date__range: list):
        return self.collection.objects.filter(date__range=date__range)

    def get_all(self):
        arr = []
        for x in self.collection.objects.filter():
            arr.append(x)
        return arr