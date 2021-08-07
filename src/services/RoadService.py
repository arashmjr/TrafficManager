from src.repository.RoadRepository import RoadRepository
from src.domain.models.RoadDomainModel import RoadDomainModel
from django.core.handlers.wsgi import WSGIRequest


class RoadService:
    repository_road: RoadRepository

    def __init__(self, repository_road: RoadRepository):
        self.repository_road = repository_road

    def add_road(self, json: str):

        model = RoadDomainModel(json['name'], json['origin'], json['destination'], json['minimum_height'], json['width'])

        self.repository_road.insert(model)
        return True
