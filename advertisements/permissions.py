from rest_framework.permissions import BasePermission


class IsAdvertisementOwner(BasePermission):
    def has_object_permission(self, request, view, obj, user):
        return request.user.is_authenticated and obj.creator == request.user
