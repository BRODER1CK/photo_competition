from django.core.exceptions import ObjectDoesNotExist
from rest_framework import permissions

from models_app.models.user import User


class HasTokenOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            if request.headers.get('Authorization'):
                request.user = User.objects.get(token=request.headers.get('Authorization'))
            return True

        try:
            request.user = User.objects.get(token=request.headers.get('Authorization'))
            return True
        except ObjectDoesNotExist:
            return False
