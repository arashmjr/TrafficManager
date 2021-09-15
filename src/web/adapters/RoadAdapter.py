from src.domain.models.DriverDomainModel import DriverDomainModel
import datetime


def road_adapter(item):

    name = item.get('name')
    width = item.get('width')
    geom = item.get('geom')
    print(geom)
    print(type(geom))
    return {"name": name, "origin": None, "destination": None, "minimum_height": None, "width": width, "geom": geom}


