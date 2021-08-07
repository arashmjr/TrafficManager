from src.repository.core.RepositoryProvider import RepositoryProvider
from src.services.AuthAdminService import AuthAdminService
from src.services.DriverService import DriverService


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




