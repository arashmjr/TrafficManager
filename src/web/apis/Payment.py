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
        return get_vehicle_payment(request)

    if request.method == 'POST':
        return add_payment(request)


def add_payment(request):
    json_data = json.loads(request.body)

    try:
        service = ServiceProvider().make_payment_service()
        service.add_payment(json_data)
        response = BaseResponse({}, True, MessageIds.SUCCESS)
        return JsonResponse(response.serialize(), safe=False, status=status.HTTP_201_CREATED)

    except ValueError:
        response = BaseError(MessageIds.ERROR_BAD_JSON)
        return JsonResponse(response.serialize(), status=status.HTTP_400_BAD_REQUEST)


def get_vehicle_payment(request):
    date_range = request.GET.getlist("Date")
    print(date_range)
    plate_number = request.GET.get("plate_number")

    try:
        service = ServiceProvider().make_payment_service()
        payments = service.get_vehicle_payment_by_date(date_range, int(plate_number))
        response = BaseResponse(payments, True, MessageIds.SUCCESS)
        return JsonResponse(response.serialize(), safe=False, status=status.HTTP_200_OK)

    except ValueError:
        response = BaseError(MessageIds.ERROR_BAD_JSON)
        return JsonResponse(response.serialize(), status=status.HTTP_400_BAD_REQUEST)

