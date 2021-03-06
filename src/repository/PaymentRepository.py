from django.db.models.manager import Manager
from src.domain.models.PaymentDomainModel import PaymentDomainModel


class PaymentRepository:
    collection: Manager

    def __init__(self, collection: Manager):
        self.collection = collection

    def insert(self, model: PaymentDomainModel):
        result = self.collection.objects.create(**model.to_dict())
        return result

    def find_record_by_date_range(self, date__range: list, plate_number: int):
        return self.collection.objects.filter(date__range=date__range, plate_number=plate_number)

    def get_payments_by(self, *args, **kwargs):
        return self.collection.objects.filter(*args, **kwargs)

    def get_all(self):
        arr = []
        for x in self.collection.objects.filter():
            arr.append(x)
        return arr

    def join_vehicle_and_payment(self):
        join_tables = self.collection.objects.filter(status__icontains='notpaid', value__gte=500) \
            .select_related('plate_number',
                            'plate_number__national_code',
                            'plate_number__national_code')
        sorted_by_value = join_tables.order_by('value')

        return sorted_by_value


