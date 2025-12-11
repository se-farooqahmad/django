from rest_framework import permissions
from rest_framework.permissions import BasePermission
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User, Group, Permission

from django.http import Http404

from .models import Blog


class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_staff)


class IsAdminUser(BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            # return True
            return bool(request.user and request.user.is_superuser)


class IsAdminOrStaffUser(BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(request.user and (request.user.is_superuser or request.user.is_staff))


class IsCreatorOrAdminOrStaffUser(permissions.BasePermission):
    """
    Custom permission to only allow the creator or admin/staff users to edit/delete a model.
    """

    def has_object_permission(self, request, view, obj):
        # Allow GET request (read-only)
        if request.method in permissions.SAFE_METHODS:
            return True

        if request.method == 'DELETE':
            if request.user.id == obj.author.id:
                return [CanDeleteBlog]

        # Allow if the user is the creator of the comment or is an admin/staff user
        return bool(obj.author == request.user or request.user.is_superuser or request.user.is_staff)





class CanAddBlog(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('crud_api.can_add_blog')

class CanChangeBlog(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('crud_api.can_change_blog')

class CanDeleteBlog(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('crud_api.can_delete_blog')

class CanViewBlog(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('crud_api.can_view_blog')




# add_permission = Permission.objects.get(codename='can_add_blog')
# change_permission = Permission.objects.get(codename='can_change_blog')
# delete_permission = Permission.objects.get(codename='can_delete_blog')
# view_permission = Permission.objects.get(codename='can_view_blog')


# user = User.objects.get(username='farooq')
# user.user_permissions.add(add_permission)


# user.user_permissions.add(add_permission, change_permission, delete_permission, view_permission)

