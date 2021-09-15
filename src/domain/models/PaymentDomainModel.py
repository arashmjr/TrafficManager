from src.domain.entities.Vehicle import Vehicle
from src.domain.entities.TollStation import TollStation
from spatialapp.domain.entities.Road import Road
import datetime


class PaymentDomainModel:
    plate_number: int
    toll_id: int
    value: int
    date: datetime
    status: str

    def __init__(self, plate_number: int, toll_id: int, value: int, date: datetime, status: str):

        self.plate_number = plate_number
        self.toll_id = toll_id
        self.value = value
        self.date = date
        self.status = status

    def to_dict(self):
        return {
                "plate_number": Vehicle(self.plate_number),
                "toll_id": TollStation(self.toll_id),
                "value": self.value,
                "date": self.date,
                "status": self.status

                }

    @staticmethod
    def asJSON(payments):
        list_payments = []
        for item in payments:
            result = {

                'plate_number': item.plate_number.plate_number,
                'toll_id': item.toll_id.toll_id,
                'value': item.value,
                'date': item.date,
                'status': item.status
            }
            list_payments.append(result)
        return list_payments

    @staticmethod
    def as_json(payments):
        list_payments = []
        for item in payments:
            result = {
                'national_code': item.plate_number.national_code.national_code,
                'plate_number': item.plate_number.plate_number,
                'value': item.value,
                'status': item.status
            }
            list_payments.append(result)
        return list_payments
