from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from school.models.appSetting_model import AppSetting
from api.serializers.app_setting_serializer import AppSettingSerializer


@csrf_exempt
def app_setting_list(request):
    if request.method == 'GET':
        app_setting = AppSetting.objects.all()
        serializer = AppSettingSerializer(app_setting, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AppSettingSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)