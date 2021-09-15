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
        return get_vehicles(request)

    if request.method == 'POST':
        return add_vehicle(request)


def add_vehicle(request: WSGIRequest):
    json_data = json.loads(request.body)
    try:
        service = ServiceProvider().make_vehicle_service()
        service.add_vehicle(json_data)
        response = BaseResponse({}, True, MessageIds.SUCCESS)
        return JsonResponse(response.serialize(), safe=False, status=status.HTTP_201_CREATED)

    except ValueError:
        response = BaseError(MessageIds.ERROR_BAD_JSON)
        return JsonResponse(response.serialize(), status=status.HTTP_400_BAD_REQUEST)


def get_vehicles(request: WSGIRequest):
    try:

        service = ServiceProvider().make_vehicle_service()
        colors = request.GET.getlist("colors")

        if colors != []:
            vehicles = service.get_vehicles_by_color(colors)
            response = BaseResponse(vehicles, True, MessageIds.SUCCESS)
            return JsonResponse(response.serialize(), safe=False, status=status.HTTP_200_OK)

        age = request.GET.get("age")
        if age is not None:
            vehicles = service.get_vehicles_by_age(age)
            response = BaseResponse(vehicles, True, MessageIds.SUCCESS)
            return JsonResponse(response.serialize(), safe=False, status=status.HTTP_200_OK)

    except ValueError:
        response = BaseError(MessageIds.ERROR_BAD_JSON)
        return JsonResponse(response.serialize(), status=status.HTTP_400_BAD_REQUEST)



