from src.repository.DriverRepository import DriverRepository
from src.domain.models.DriverDomainModel import DriverDomainModel
from django.core.handlers.wsgi import WSGIRequest


class DriverService:
    repository_driver: DriverRepository

    def __init__(self, repository_driver: DriverRepository):

        self.repository_driver = repository_driver

    def add_driver(self, json: str):
        print('s')
        model = DriverDomainModel(json['name'], json['birthdate'], json['national_code'])
        self.repository_driver.insert(model)

        return True
