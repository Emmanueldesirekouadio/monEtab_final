from rest_framework import serializers
from school.models.appSetting_model import AppSetting


class AppSettingSerializer(serializers.ModelSerializer):

    class Meta:
        model = AppSetting
        fields = "__all__"