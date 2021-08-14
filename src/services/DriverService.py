from src.repository.DriverRepository import DriverRepository
from src.repository.PaymentRepository import PaymentRepository
from src.domain.models.DriverDomainModel import DriverDomainModel
from src.domain.models.PaymentDomainModel import PaymentDomainModel


class DriverService:
    repository_driver: DriverRepository
    repository_payment: PaymentRepository

    def __init__(self, repository_driver: DriverRepository, repository_payment: PaymentRepository):

        self.repository_driver = repository_driver
        self.repository_payment = repository_payment

    def add_driver(self, json):

        model = DriverDomainModel(json['name'], json['birthdate'], json['national_code'])
        self.repository_driver.insert(model)
        return True

    def get_owners_by_notpaid_status(self):
        sorted_query_by_value = self.repository_payment.join_vehicle_and_payment()
        filtered_results = PaymentDomainModel.as_json(sorted_query_by_value)
        print(filtered_results)

        objects_owners = []
        for item in filtered_results:
            obj_driver = self.repository_driver.find_record_by_id(item['owner_id'])
            objects_owners.append(obj_driver)

        list_owners = DriverDomainModel.asJSON(objects_owners)
        return list_owners






