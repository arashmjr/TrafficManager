from django.core.handlers.wsgi import WSGIRequest
from src.services.core.ServiceProvider import ServiceProvider
from src.web.dtos.BaseResponse import BaseResponse, BaseError
from src.web.utils.Localizations import MessageIds
from rest_framework import status
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from src.services.Manager.AuthorizationManager import is_admin_only
import json
from src.web.adapters.OwnerAdapter import owner_adapter
from src.web.adapters.VehicleAdapter import vehicle_adapter


@is_admin_only
@csrf_exempt
def handler(request):
    if request.method == 'POST':
        return add_drivers(request)

    if request.method == 'GET':
        return get_owners_by_notpaid_status(request)


def add_drivers(request: WSGIRequest):
    json_data = json.loads(request.body)

    try:
        service_owner = ServiceProvider().make_driver_service()
        service_vehicle = ServiceProvider().make_vehicle_service()
        requestType = request.GET.get('requestType')

        if requestType == '1':

            adapted_list_owner = list(map(owner_adapter, json_data))
            # adapted_list_vehicle = list(map(vehicle_adapter, json_data))
            adapted_list_vehicle = vehicle_adapter(json_data)

            service_owner.add_list_of_owners(adapted_list_owner)
            service_vehicle.add_list_of_vehicles(adapted_list_vehicle)
            response = BaseResponse({}, True, MessageIds.SUCCESS)
            return JsonResponse(response.serialize(), safe=False, status=status.HTTP_201_CREATED)

        if requestType == '2':
            service_owner.add_driver(json_data)
            response = BaseResponse({}, True, MessageIds.SUCCESS)
            return JsonResponse(response.serialize(), safe=False, status=status.HTTP_201_CREATED)

    except ValueError:
        response = BaseError(MessageIds.ERROR_BAD_JSON)
        return JsonResponse(response.serialize(), status=status.HTTP_400_BAD_REQUEST)


def get_owners_by_notpaid_status(request: WSGIRequest):
    try:
        service = ServiceProvider().make_driver_service()

        owners = service.get_owners_by_notpaid_status()
        response = BaseResponse(owners, True, MessageIds.SUCCESS)
        return JsonResponse(response.serialize(), safe=False, status=status.HTTP_200_OK)

    except ValueError:
        response = BaseError(MessageIds.ERROR_BAD_JSON)
        return JsonResponse(response.serialize(), status=status.HTTP_400_BAD_REQUEST)


