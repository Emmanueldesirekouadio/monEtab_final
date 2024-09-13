from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from user.models.roleUser_model import RoleUser
from api.serializers.role_user_serializer import RoleUserSerializer


@csrf_exempt
def role_user_list(request):
    if request.method == 'GET':
        role_users = RoleUser.objects.all()
        serializer = RoleUserSerializer(role_users, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = RoleUserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)