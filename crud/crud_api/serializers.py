from rest_framework import serializers
from .models import Blog
from django.contrib.auth.models import User, Group, Permission
from django.conf import settings
from django.http import HttpResponseForbidden   

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'


class ContentPermissionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = "__all__"

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'id', 'is_staff', 'is_superuser', 'username','password', 'email']
        
    def validate(self, attrs):
        if 'email' not in attrs or not attrs['email']:
            raise serializers.ValidationError("Email is required.")
        user_email = attrs['email']
        email_domain = user_email.split('@')[-1]
        print(user_email)
        print(email_domain)
        if email_domain not in settings.ALLOWED_EMAIL_DOMAINS:
            raise serializers.ValidationError("Only Allowed Domained Email ")
        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
        
class GroupSerializer(serializers.HyperlinkedModelSerializer):
    permissions = ContentPermissionsSerializer(many=True, read_only=True)
    class Meta:
        model = Group
        fields = ['url', 'name', 'permissions']

class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ['id', 'name', 'content_type', 'codename']
