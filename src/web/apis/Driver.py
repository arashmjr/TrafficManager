from src.services.core.ServiceProvider import ServiceProvider
from src.web.dtos.BaseResponse import BaseResponse, BaseError
from src.web.utils.Localizations import MessageIds
from rest_framework import status
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def add_driver(request):
    print('h')
    json_data = json.loads(request.body)
    print('hello')
    try:
        service = ServiceProvider().make_driver_service()
        service.add_driver(json_data)
        response = BaseResponse({}, True, MessageIds.SUCCESS)
        return JsonResponse(response.serialize(), safe=False, status=status.HTTP_201_CREATED)

    except ValueError:
        response = BaseError(MessageIds.ERROR_BAD_JSON)
        return JsonResponse(response.serialize(), status=status.HTTP_400_BAD_REQUEST)