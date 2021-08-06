# from Src.repository.SaveUserRepository import SaveUserRepository
# from Src.repository.ProductRepository import ProductRepository
# from Src.repository.CartRepository import CartRepository
# from Src.repository.CartProductRepository import CartProductRepository
# from Src.repository.OrderRepository import OrderRepository
from src.repository.AdminUserRepository import AdminUserRepository
from src.repository.core.CoreDatabase import CoreDatabase
from src.domain.entities.AdminUser import Admin


class RepositoryProvider:
    database = CoreDatabase.get_instance()

    def make_admin_profile(self):
        collection = Admin
        return AdminUserRepository(collection)


