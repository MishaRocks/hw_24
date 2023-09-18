from rest_framework.permissions import BasePermission


class IsModerator(BasePermission):

    def has_permission(self, request, view):
        if request.user.groups.filter(name='Moderators'):
            return True


class IsOwner(BasePermission):

    def has_permission(self, request, view):
        if request.user == view.get_object().user:
            return True
