from rest_framework.permissions import BasePermission


class ModeratorAndObjectOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.groups.filter(name='moderators').exists() and request.method in ['GET', 'PUT', 'PATCH']:
            return True
        if request.user == obj.creator:
            return True
        return False
