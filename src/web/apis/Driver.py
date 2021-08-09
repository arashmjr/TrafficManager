from django.core.handlers.wsgi import WSGIRequest
from src.services.core.ServiceProvider import ServiceProvider
from src.web.dtos.BaseResponse import BaseResponse, BaseError
from src.web.utils.Localizations import MessageIds
from rest_framework import status
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from src.services.Manager.AuthorizationManager import is_admin_only
import json


# @is_admin_only
@csrf_exempt
def handler(request):
    if request.method == 'POST':
        return add_drivers(request)


def add_drivers(request: WSGIRequest):
    json_data = json.loads(request.body)

    try:
        service = ServiceProvider().make_driver_service()
        service.add_driver(json_data)
        response = BaseResponse({}, True, MessageIds.SUCCESS)
        return JsonResponse(response.serialize(), safe=False, status=status.HTTP_201_CREATED)

    except ValueError:
        response = BaseError(MessageIds.ERROR_BAD_JSON)
        return JsonResponse(response.serialize(), status=status.HTTP_400_BAD_REQUEST)
