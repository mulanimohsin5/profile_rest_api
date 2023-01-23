from rest_framework import permissions


class UpdateOwnProfilePerm(permissions.BasePermission):
    """ Allow user to update their own profile."""

    def has_object_permission(self, request, view, obj):
        """ Ckeck user tring to edit thier own profile."""

        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.id == request.user.id