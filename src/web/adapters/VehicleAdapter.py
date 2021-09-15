from src.domain.models.VehicleDomainModel import VehicleDomainModel
import datetime
from src.domain.entities.Driver import Driver


def vehicle_adapter(json_data):
    vehicles = []
    for item in json_data:
        national_code = item.get('national_code')
        ownerCar = item.get('ownerCar')
        for segment in ownerCar:
            plate_number = segment.get('id')
            height = segment.get('length')
            weight = segment.get('load_valume')
            vehicle = {"plate_number": plate_number, "national_code": national_code,"color": segment.get("color"),
                   "type": segment.get("type"), "height": height, "weight": weight, "model": None, "year": None}

            vehicles.append(vehicle)
    # print(vehicles)
    return vehicles






