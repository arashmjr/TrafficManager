from src.repository.RoadRepository import RoadRepository
from src.domain.models.RoadDomainModel import RoadDomainModel
from django.core.handlers.wsgi import WSGIRequest


class RoadService:
    repository_road: RoadRepository

    def __init__(self, repository_road: RoadRepository):
        self.repository_road = repository_road

    def add_road(self, json):
        # self.repository_road.remove_all()
        model = RoadDomainModel(json['name'], json['origin'], json['destination'], json['minimum_height'], json['width'],
                                json['geom'])

        self.repository_road.insert(model)
        return True

    def add_list_of_roads(self, adapted_list):
        for item in adapted_list:
            model = RoadDomainModel(item['name'], item['origin'], item['destination'],item['minimum_height'],
                                    item['width'], item['geom'])

            self.repository_road.insert(model)


