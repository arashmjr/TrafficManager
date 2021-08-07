from src.repository.AdminUserRepository import AdminUserRepository
from src.repository.DriverRepository import DriverRepository
from src.repository.core.CoreDatabase import CoreDatabase
from src.domain.entities.AdminUser import Admin
from src.domain.entities.Driver import Driver


class RepositoryProvider:
    database = CoreDatabase.get_instance()

    def make_admin_profile(self):
        collection = Admin
        return AdminUserRepository(collection)

    def make_driver(self):
        collection = Driver
        return DriverRepository(collection)



