from rest_framework import permissions


class HasTokenOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        return bool(request.headers.get('Authorization') == request.user.token)
