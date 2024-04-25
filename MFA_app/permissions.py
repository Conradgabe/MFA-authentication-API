from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied

from .models import CustomUser

class BlockUnverifiedEmail(permissions.BasePermission):
    """
    Permission to block unverified Email account
    """
    message = "User email has not been verified"
    
    def has_permission(self, request, view):
        email = request.data.get('email')
        if email:
            filtered_email = CustomUser.objects.filter(email=email).first()

            if filtered_email and filtered_email.is_verified():
                return True

        return False
