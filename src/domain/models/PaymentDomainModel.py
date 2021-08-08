from src.domain.entities.Vehicle import Vehicle
from src.domain.entities.TollStation import TollStation
from src.domain.entities.Road import Road
import datetime


class PaymentDomainModel:
    vehicle_id: int
    toll_id: int
    road_id: int
    value: int
    date: datetime
    status: str

    def __init__(self, vehicle_id: int, toll_id: int, road_id: int, value: int, date: datetime, status: str):

        self.vehicle_id = vehicle_id
        self.toll_id = toll_id
        self.road_id = road_id
        self.value = value
        self.date = date
        self.status = status

    def to_dict(self):
        return {
                "vehicle_id": Vehicle(self.vehicle_id),
                "toll_id": TollStation(self.toll_id),
                "road_id": Road(self.road_id),
                "value": self.value,
                "date": self.date,
                "status": self.status

                }

    @staticmethod
    def asJSON(payments):
        list_payments = []
        for item in payments:
            result = {

                'vehicle_id': item.vehicle_id.vehicle_id,
                'toll_id': item.toll_id.toll_id,
                'road_id': item.road_id.road_id,
                'value': item.value,
                'date': item.date,
                'status': item.status
            }
            list_payments.append(result)
        return list_payments
