from rest_framework import serializers
from user.models.user_model import UserApps


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserApps
        fields = "__all__"