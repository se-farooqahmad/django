from django.contrib.auth.models import User, Group, Permission
from rest_framework import serializers


class ContentPermissionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = "__all__"

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'id', 'is_staff', 'is_superuser', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    permissions = ContentPermissionsSerializer(many=True, read_only=True)
    class Meta:
        model = Group
        fields = ['url', 'name', 'permissions']