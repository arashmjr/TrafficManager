from src.repository.AdminUserRepository import AdminUserRepository
from src.repository.DriverRepository import DriverRepository
from src.repository.VehicleRepository import VehicleRepository
from src.repository.core.CoreDatabase import CoreDatabase
from src.domain.entities.AdminUser import Admin
from src.domain.entities.Driver import Driver
from src.domain.entities.Vehicle import Vehicle
from src.domain.entities.Road import Road
from src.domain.entities.TollStation import TollStation
from src.repository.RoadRepository import RoadRepository
from src.repository.TollRepository import TollRepository


class RepositoryProvider:
    database = CoreDatabase.get_instance()

    def make_admin_profile(self):
        collection = Admin
        return AdminUserRepository(collection)

    def make_driver(self):
        collection = Driver
        return DriverRepository(collection)

    def make_vehicle(self):
        collection = Vehicle
        return VehicleRepository(collection)

    def make_road(self):
        collection = Road
        return RoadRepository(collection)

    def make_Toll(self):
        collection = TollStation
        return TollRepository(collection)
    






