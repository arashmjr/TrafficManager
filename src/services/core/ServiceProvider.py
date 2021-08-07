from src.repository.core.RepositoryProvider import RepositoryProvider
from src.services.AuthAdminService import AuthAdminService
from src.services.DriverService import DriverService
from src.services.VehicleService import VehicleService
from src.services.RoadService import RoadService
from src.services.TollService import TollService


class ServiceProvider:
    repository_provider: RepositoryProvider

    def __init__(self):
        self.repository_provider = RepositoryProvider()

    def make_signup_admin_service(self):
        return AuthAdminService(self.repository_provider.make_admin_profile())

    def make_login_admin_service(self):
        return AuthAdminService(self.repository_provider.make_admin_profile())

    def make_driver_service(self):
        return DriverService(self.repository_provider.make_driver())

    def make_vehicle_service(self):
        return VehicleService(self.repository_provider.make_vehicle())

    def make_road_service(self):
        return RoadService(self.repository_provider.make_road())

    def make_toll_service(self):
        return TollService(self.repository_provider.make_Toll())




