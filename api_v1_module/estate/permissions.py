from rest_framework.permissions import BasePermission


class IsConsultantUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_consultant

class IsOwnerEstateAd(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.consultant == request.user
