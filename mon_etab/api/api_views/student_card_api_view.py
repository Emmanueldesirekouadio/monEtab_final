from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from student.models.studentCards_model import StudentCards
from api.serializers.student_card_serializer import StudentCardSerializer


@csrf_exempt
def student_card_list(request):
    if request.method == 'GET':
        student_card = StudentCards.objects.all()
        serializer = StudentCardSerializer(student_card, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = StudentCardSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)