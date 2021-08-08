from src.services.core.ServiceProvider import ServiceProvider
from src.web.dtos.BaseResponse import BaseResponse, BaseError
from src.web.utils.Localizations import MessageIds
from rest_framework import status
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def add_traffic_log(request):
    json_data = json.loads(request.body)

    try:
        service = ServiceProvider().make_traffic_log_service()
        service.add_traffic_log(json_data)
        response = BaseResponse({}, True, MessageIds.SUCCESS)
        return JsonResponse(response.serialize(), safe=False, status=status.HTTP_201_CREATED)

    except ValueError:
        response = BaseError(MessageIds.ERROR_BAD_JSON)
        return JsonResponse(response.serialize(), status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def get_logs_by_type_width(self):

    try:
        service = ServiceProvider().make_traffic_log_service()
        vehicles = service.get_logs_by_type_width()
        response = BaseResponse(vehicles, True, MessageIds.SUCCESS)
        return JsonResponse(response.serialize(), safe=False, status=status.HTTP_201_CREATED)

    except ValueError:
        response = BaseError(MessageIds.ERROR_BAD_JSON)
        return JsonResponse(response.serialize(), status=status.HTTP_400_BAD_REQUEST)
