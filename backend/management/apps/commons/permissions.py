from rest_framework.permissions import BasePermission

from management.apps.profiles.choices import RoleProfile


class IsAdminAuthenticated(BasePermission):
    """
    Allows admin.
    """

    def has_permission(self, request, view):
        return request.user.profile.role == RoleProfile.ADMIN and request.user.is_authenticated
