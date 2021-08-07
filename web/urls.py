from django.conf.urls import url
from src.web.apis import AdminAuth, Driver


urlpatterns = [
    url(r'^SignupAdmin/$', AdminAuth.sign_up_admin),
    url(r'^LoginAdmin/$', AdminAuth.login_admin),
    url(r'^AddDriver/$', Driver.add_driver),

]

