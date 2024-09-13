from rest_framework import serializers
from user.models.roleUser_model import RoleUser


class RoleUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = RoleUser
        fields = "__all__"