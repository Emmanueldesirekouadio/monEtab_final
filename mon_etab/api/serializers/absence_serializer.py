from rest_framework import serializers
from student.models.absence_model import Absence


class AbsenceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Absence
        fields = "__all__"