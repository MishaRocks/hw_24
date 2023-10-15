from rest_framework.permissions import BasePermission


class NotModerator(BasePermission):
    def has_permission(self, request, view):
        if request.user.groups.filter(name='moderators').exists():
            return False
        return True


class IsModerator(BasePermission):

    def has_permission(self, request, view):
        if request.user.groups.filter(name='moderators'):
            return True


class IsOwner(BasePermission):

    def has_permission(self, request, view):
        if request.user == view.get_object().user:
            return True
