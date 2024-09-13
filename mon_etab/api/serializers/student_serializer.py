from rest_framework import serializers
from student.models.student_model import Student


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = "__all__"