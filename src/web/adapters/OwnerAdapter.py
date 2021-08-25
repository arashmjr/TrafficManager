from src.domain.models.DriverDomainModel import DriverDomainModel
import datetime


def owner_adapter(item):

    now = datetime.datetime.now()
    birthdate = now.year - item.get('age')
    return {"national_code": item.get('national_code'), "name": item.get("name"), "birthdate": birthdate}



