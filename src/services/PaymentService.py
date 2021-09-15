from src.repository.PaymentRepository import PaymentRepository
from src.domain.models.PaymentDomainModel import PaymentDomainModel
import datetime


class PaymentService:
    repository_payment: PaymentRepository

    def __init__(self, repository_payment: PaymentRepository):
        self.repository_payment = repository_payment

    def add_payment(self, json):

        date = datetime.date.today()
        model = PaymentDomainModel(json['plate_number'], json['toll_id'], json['value'], date,
                                   json['status'])
        print(model.to_dict())
        self.repository_payment.insert(model)
        return True

    def get_vehicle_payment_by_date(self, range_date, plate_number):

        objects = self.repository_payment.find_record_by_date_range(range_date, plate_number)
        records = PaymentDomainModel.asJSON(objects)
        return records








