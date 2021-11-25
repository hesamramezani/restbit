from rest_framework.permissions import BasePermission
from django.contrib.auth.models import User

class IsSuperUser(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)

    """
    its custom permission just for superuser
    """


class IsOwner(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user == User.objects.get(pk=view.kwargs['pk']))

    """
    its custom permission just for ownuser that make user
    """





