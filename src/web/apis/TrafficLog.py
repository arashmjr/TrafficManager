from django.core.handlers.wsgi import WSGIRequest

from src.services.Manager.AuthorizationManager import is_admin_only
from src.services.core.ServiceProvider import ServiceProvider
from src.web.dtos.BaseResponse import BaseResponse, BaseError
from src.web.utils.Localizations import MessageIds
from rest_framework import status
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


# @is_admin_only
@csrf_exempt
def handler(request):
    if request.method == 'GET':
        return get_logs(request)

    if request.method == 'POST':
        return add_logs(request)


def add_logs(request: WSGIRequest):
    json_data = json.loads(request.body)

    try:
        service = ServiceProvider().make_traffic_log_service()
        service.add_traffic_log(json_data)
        response = BaseResponse({}, True, MessageIds.SUCCESS)
        return JsonResponse(response.serialize(), safe=False, status=status.HTTP_201_CREATED)

    except ValueError:
        response = BaseError(MessageIds.ERROR_BAD_JSON)
        return JsonResponse(response.serialize(), status=status.HTTP_400_BAD_REQUEST)


def get_logs(request: WSGIRequest):

    try:
        service = ServiceProvider().make_traffic_log_service()
        max_road_width = request.GET.get("maxRoadWidth")
        vehicle_type = request.GET.get("vehicleType")

        if max_road_width is not None and vehicle_type is not None:
            logs = service.get_logs_by(max_road_width=max_road_width, vehicle_type=vehicle_type)
            response = BaseResponse(logs, True, MessageIds.SUCCESS)
            return JsonResponse(response.serialize(), safe=False, status=status.HTTP_201_CREATED)

        # province = tehran & tollStationName = 1 & distance = 600

        province = request.GET.get("province")
        toll_station_name = request.GET.get("tollStationName")
        distance = request.GET.get("distance")
        vehicle_type = request.GET.get("vehicleType")

        if province is not None and toll_station_name is not None and distance is not None and vehicle_type is not None:
            logs = service.get_logs_near_toll_station(province, distance, toll_station_name, vehicle_type)
            response = BaseResponse(logs, True, MessageIds.SUCCESS)
            return JsonResponse(response.serialize(), safe=False, status=status.HTTP_201_CREATED)

    except ValueError:
        response = BaseError(MessageIds.ERROR_BAD_JSON)
        return JsonResponse(response.serialize(), status=status.HTTP_400_BAD_REQUEST)

