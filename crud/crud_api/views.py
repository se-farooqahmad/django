from rest_framework import viewsets
from .models import Blog
from .serializers import BlogSerializer
from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group, Permission

from .serializers import *
from rest_framework import permissions

from django.http import Http404
from rest_framework import permissions
from rest_framework.permissions import BasePermission
from django.shortcuts import get_object_or_404
from django.http import Http404


from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdminOrReadOnly, IsAdminUser, IsAdminOrStaffUser, IsCreatorOrAdminOrStaffUser

from rest_framework import generics
from .permissions import CanAddBlog, CanChangeBlog, CanDeleteBlog, CanViewBlog




class BlogViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    def get_queryset(self):
        queryset = Blog.objects.all()
        name = self.request.query_params.get('name')
        author = self.request.query_params.get('author')

        if name:
            queryset = queryset.filter(name__icontains=name)
        
        return queryset
    
    # permission_classes = [IsCreatorOrAdminOrStaffUser]
    permission_classes = [permissions.IsAuthenticated,IsCreatorOrAdminOrStaffUser]
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    



class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAdminUser and IsAuthenticated]

class PermissionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    # queryset = Permission.objects.filter(content_type=7)
    # queryset = Permission.objects.all()
    excluded_apps = ['admin', 'auth', 'contenttypes', 'sessions']
        
    queryset = Permission.objects.exclude(
            content_type__app_label__in = excluded_apps
    )
    serializer_class = PermissionSerializer
    permission_classes = [permissions.IsAuthenticated and IsAdminUser]



class BlogCreateView(generics.CreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [CanAddBlog]

class BlogRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [CanChangeBlog, CanDeleteBlog, CanViewBlog]

