from rest_framework import permissions
from rest_framework.views import View


class IsAdminOrRead(permissions.BasePermission):
    def has_permission(self, request, view: View) -> bool:
        return request.user.is_superuser or request.method == "GET"
