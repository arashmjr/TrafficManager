from src.services.Manager.AuthorizationManager import is_admin_only
from src.services.core.ServiceProvider import ServiceProvider
from src.web.dtos.BaseResponse import BaseResponse, BaseError
from src.web.utils.Localizations import MessageIds
from rest_framework import status
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from src.web.adapters.RoadAdapter import road_adapter
import json


# @is_admin_only
@csrf_exempt
def handler(request):
    if request.method == 'POST':
        return add_road(request)


def add_road(request):
    json_data = json.loads(request.body)
    requestType = request.GET.get('requestType')
    try:
        service = ServiceProvider().make_road_service()
        if requestType == '1':
            road_adapter(json_data)

        if requestType == '2':
            service.add_road(json_data)
            response = BaseResponse({}, True, MessageIds.SUCCESS)
            return JsonResponse(response.serialize(), safe=False, status=status.HTTP_201_CREATED)

    except ValueError:
        response = BaseError(MessageIds.ERROR_BAD_JSON)
        return JsonResponse(response.serialize(), status=status.HTTP_400_BAD_REQUEST)
