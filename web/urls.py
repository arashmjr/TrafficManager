from django.conf.urls import url
from src.web.apis import AdminAuth, Driver, Vehicle, Road, TollStation, TrafficLog


urlpatterns = [
    url(r'^SignupAdmin/$', AdminAuth.sign_up_admin),
    url(r'^LoginAdmin/$', AdminAuth.login_admin),
    url(r'^AddDriver/$', Driver.add_driver),
    url(r'^AddVehicle/$', Vehicle.add_vehicle),
    url(r'^AddRoad/$', Road.add_road),
    url(r'^AddTollStation/$', TollStation.add_toll),
    url(r'^GetVehiclesByColor/$', Vehicle.get_vehicles_by_color),
    url(r'^GetVehiclesByAge/$', Vehicle.get_vehicles_by_age),
    url(r'^AddTrafficLog/$', TrafficLog.add_traffic_log),

]

