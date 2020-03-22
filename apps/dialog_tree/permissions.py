"""`dialog_tree` app permissions."""
from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """

    def has_object_permission(self, request, view, obj):
        """Allowing only only owner to edit object."""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.owner == request.user
