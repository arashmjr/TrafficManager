from src.repository.PaymentRepository import PaymentRepository
from src.domain.models.VehicleDomainModel import VehicleDomainModel
from src.domain.models.PaymentDomainModel import PaymentDomainModel
from django.core.handlers.wsgi import WSGIRequest
from itertools import chain
import datetime


class PaymentService:
    repository_payment: PaymentRepository

    def __init__(self, repository_payment: PaymentRepository):
        self.repository_payment = repository_payment

    def add_payment(self, json: str):

        date = datetime.date.today()
        model = PaymentDomainModel(json['vehicle_id'], json['toll_id'], json['road_id'], json['value'], date,
                                   json['status'])

        self.repository_payment.insert(model)
        return True

    def get_vehicle_payment(self, json: str):

        objects = self.repository_payment.find_record_by_date_range([json['start_date'], json['end_date']])
        records = PaymentDomainModel.asJSON(objects)
        return records






