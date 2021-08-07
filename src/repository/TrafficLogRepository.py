from django.db.models.manager import Manager
from src.domain.models.TrafficLogDomainModel import TrafficLogDomainModel


class TrafficLogRepository:
    collection: Manager

    def __init__(self, collection: Manager):
        self.collection = collection

    def insert(self, model: TrafficLogDomainModel):
        result = self.collection.objects.create(**model.to_dict())
        return result
