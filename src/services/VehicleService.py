from src.repository.VehicleRepository import VehicleRepository
from src.repository.DriverRepository import DriverRepository
from src.domain.models.VehicleDomainModel import VehicleDomainModel
from src.domain.models.DriverDomainModel import DriverDomainModel
from django.core.handlers.wsgi import WSGIRequest
from itertools import chain
import datetime


class VehicleService:
    repository_vehicle: VehicleRepository
    repository_driver: DriverRepository

    def __init__(self, repository_vehicle: VehicleRepository, repository_driver: DriverRepository):
        self.repository_vehicle = repository_vehicle
        self.repository_driver = repository_driver

    def add_vehicle(self, json: str):

        model = VehicleDomainModel(json['owner_id'], json['color'], json['type'], json['weight'],
                                  json['height'], json['model'], json['year'])

        documents = self.repository_vehicle.find_record_by_owner_id(model.owner_id)
        records = VehicleDomainModel.asJSON(documents)
        if records is not None:
            for item in records:
                if item['type'] == 'heavy':
                    raise Exception("Sorry, this owner can't have more than one heavy vehicle")

        self.repository_vehicle.insert(model)
        return True

    def get_vehicles_by_color(self):
        vehicle_red = self.repository_vehicle.find_record_by_color('red')
        vehicle_blue = self.repository_vehicle.find_record_by_color('blue')
        vehicles = list(chain(vehicle_red, vehicle_blue))
        list_vehicle = VehicleDomainModel.asJSON(vehicles)

        return list_vehicle

    def get_vehicles_by_age(self):

        drivers = self.repository_driver.get_all()
        list_drivers = DriverDomainModel.asJSON(drivers)
        date = datetime.date.today().year
        arr_drivers = []
        for item in list_drivers:
            Age = int(date) - item['birthdate']
            if Age > 70:
                arr_drivers.append(item)

        obj_vehicles = self.repository_vehicle.find_record_by_list_owner_id(arr_drivers)
        list_vehicles = VehicleDomainModel.asJSON(obj_vehicles)
        print(list_vehicles)
        return list_vehicles

