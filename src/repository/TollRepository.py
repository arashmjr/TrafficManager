from django.db.models.manager import Manager
from src.domain.models.TollDomainModel import TollDomainModel


class TollRepository:
    collection: Manager

    def __init__(self, collection: Manager):
        self.collection = collection

    def insert(self, model: TollDomainModel):
        result = self.collection.objects.create(**model.to_dict())
        return result
