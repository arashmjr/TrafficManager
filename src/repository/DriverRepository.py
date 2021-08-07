from django.db.models.manager import Manager
from src.domain.models.DriverDomainModel import DriverDomainModel


class DriverRepository:
    collection: Manager

    def __init__(self, collection: Manager):
        self.collection = collection

    def insert(self, model: DriverDomainModel):
        result = self.collection.objects.create(**model.to_dict())
        return result

    # def find_record_by_user_id(self, user_id: int):
    #     result = self.collection.objects.filter(user_id=user_id)
    #     return result
    #
    # def find_record_by_email(self, email: str):
    #     return self.collection.objects.get(email=email)
    #
    # def find_record_by_email_signup(self, email: str):
    #     return self.collection.objects.filter(email=email)
    #
    # def get_all(self):
    #     arr = []
    #     for x in self.collection.filter():
    #         arr.append(x)
    #     return arr
    #
    # def remove_record(self, user_id:  int):
    #     return self.collection.objects.filter(user_id=user_id).delete()
    #
    # def remove_all(self):
    #     delete_all = self.collection.all().delete()
    #     return delete_all
