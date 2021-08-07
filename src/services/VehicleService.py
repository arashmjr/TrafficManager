# from Src.repository.CartRepository import CartRepository
# from Src.Domain.models.CartDomainModel import CartDomainModel
# from Src.repository.CartProductRepository import CartProductRepository
# from Src.repository.ProductRepository import ProductRepository
# from Src.services.Manager.AuthorizationManager import login_required, extract_user_id
# from Src.Domain.models.CartProductDomainModel import CartProductDomainModel
# from django.core.handlers.wsgi import WSGIRequest
# import datetime
#
#
# class CartService:
#     repository_cart: CartRepository
#     repository_product: ProductRepository
#     repository_cart_product: CartProductRepository
#
#     def __init__(self, repository_cart: CartRepository, repository_product: ProductRepository,
#                  repository_cart_product: CartProductRepository):
#
#         self.repository_cart = repository_cart
#         self.repository_product = repository_product
#         self.repository_cart_product = repository_cart_product
#
#     def add_item(self, json: str, request: WSGIRequest):
#
#         # get user_id from token
#         user_id = extract_user_id(request)
#
#         # get cart_id from cart model
#         item = self.repository_cart.find_record_by_user_id(user_id)
#         cart_id = item.cart_id
#
#         creation_date = datetime.datetime.now()
#         model = CartProductDomainModel(json['product_id'], cart_id, user_id, creation_date,
#                                             json['quantity'], -1)
#
#         self.repository_cart_product.insert(model)
#
#         return True