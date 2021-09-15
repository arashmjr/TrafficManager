from django.conf.urls import url
from src.web.apis import AdminAuth, Driver, Vehicle, TollStation, TrafficLog, Payment
from spatialapp.web.apis import Road

urlpatterns = [
    url(r'^auth/admin/signup$', AdminAuth.sign_up_admin),
    url(r'^auth/admin/login$', AdminAuth.login_admin),
    url(r'^dashboard/admin/driver/$', Driver.handler),
    url(r'^dashboard/admin/vehicle/$', Vehicle.handler),
    url(r'^dashboard/admin/road/$', Road.handler),
    url(r'^dashboard/admin/tollStation/$', TollStation.handler),
    url(r'^dashboard/admin/trafficLog/$', TrafficLog.handler),
    url(r'^dashboard/admin/payment/$', Payment.handler),

]

