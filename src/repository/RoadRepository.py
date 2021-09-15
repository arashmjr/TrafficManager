from django.db.models.manager import Manager
from src.domain.models.RoadDomainModel import RoadDomainModel


class RoadRepository:
    collection: Manager

    def __init__(self, collection: Manager):
        self.collection = collection

    def insert(self, model: RoadDomainModel):
        result = self.collection.objects.create(**model.to_dict())
        return result

    def remove_all(self):
        x = self.collection.objects.all()
        y =x.delete()
        return y
