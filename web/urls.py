from django.conf.urls import url
from src.web.apis import AdminAuth, Driver, Vehicle, Road, TollStation


urlpatterns = [
    url(r'^SignupAdmin/$', AdminAuth.sign_up_admin),
    url(r'^LoginAdmin/$', AdminAuth.login_admin),
    url(r'^AddDriver/$', Driver.add_driver),
    url(r'^AddVehicle/$', Vehicle.add_vehicle),
    url(r'^AddRoad/$', Road.add_road),
    url(r'^AddTollStation/$', TollStation.add_toll),

]

