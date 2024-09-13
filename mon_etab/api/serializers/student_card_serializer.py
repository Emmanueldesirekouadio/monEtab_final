from rest_framework import serializers
from student.models.studentCards_model import StudentCards


class StudentCardSerializer(serializers.ModelSerializer):

    class Meta:
        model = StudentCards
        fields = "__all__"