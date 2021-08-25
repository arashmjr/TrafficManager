from src.domain.models.DriverDomainModel import DriverDomainModel
import datetime


def road_adapter(json_data):
    for item in json_data:
        name = item.get('name')
        width = item.get('width')
        geom = item.get('geom')
        print(geom)
        # return {"national_code": item.get('national_code'), "name": item.get("name")}
