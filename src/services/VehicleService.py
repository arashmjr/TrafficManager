from src.repository.VehicleRepository import VehicleRepository
from src.domain.models.VehicleDomainModel import VehicleDomainModel
from django.core.handlers.wsgi import WSGIRequest


class VehicleService:
    repository_vehicle: VehicleRepository

    def __init__(self, repository_vehicle: VehicleRepository):
        self.repository_vehicle = repository_vehicle

    def add_vehicle(self, json: str):

        model = VehicleDomainModel(json['owner_id'], json['color'], json['type'], json['weight'],
                                  json['height'], json['model'], json['year'])

        self.repository_vehicle.insert(model)
        return True
