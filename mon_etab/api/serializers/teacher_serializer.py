from rest_framework import serializers
from teacher.models.teacher_model import Teacher


class TeacherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teacher
        fields = "__all__"