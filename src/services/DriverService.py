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

        model = DriverDomainModel(json['national_code'], json['name'], json['birthdate'])
        self.repository_driver.insert(model)
        return True

    def add_list_of_owners(self, adapted_list):
        for item in adapted_list:
            model = DriverDomainModel(item['national_code'], item['name'], item['birthdate'])
            self.repository_driver.insert(model)

    def get_owners_by_notpaid_status(self):
        sorted_query_by_value = self.repository_payment.join_vehicle_and_payment()
        filtered_results = PaymentDomainModel.as_json(sorted_query_by_value)
        print(filtered_results)

        # objects_owners = []
        # for item in filtered_results:
        #     obj_driver = self.repository_driver.find_record_by_national_code(item['national_code'])
        #     objects_owners.append(obj_driver)
        #
        # list_owners = DriverDomainModel.asJSON(objects_owners)

        return filtered_results







