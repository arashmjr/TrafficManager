from src.repository.TollRepository import TollRepository
from src.domain.models.TollDomainModel import TollDomainModel
from django.core.handlers.wsgi import WSGIRequest


class TollStationService:
    repository_toll: TollRepository

    def __init__(self, repository_toll: TollRepository):
        self.repository_toll = repository_toll

    def add_toll_station(self, json: str):

        model = TollDomainModel(json['road_id'], json['name'], json['heavy_vehicle_charge'],
                                json['light_vehicle_charge'], json['heavy_vehicle_charge_per_kg'],
                                json['latitude'], json['longitude'])

        self.repository_toll.insert(model)
        return True
