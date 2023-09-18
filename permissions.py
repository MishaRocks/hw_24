from rest_framework.permissions import BasePermission


class IsModerator(BasePermission):

    def has_permission(self, request, view):
        if request.user.groups.filter(name='moderators'):
            return True


class IsOwner(BasePermission):

    def has_permission(self, request, view):
        if request.user == view.get_object().user:
            return True


class ModeratorAndObjectOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.groups.filter(name='moderators').exists() and request.method in ['GET', 'PUT', 'PATCH']:
            return True
        if request.user == obj.creator:
            return True
        return False
