from rest_framework.permissions import BasePermission

class AccessRights(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.profile.group == 'superuser':
            return True
        else:
            return False