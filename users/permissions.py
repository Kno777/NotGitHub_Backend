from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        
        # Read-only permissions are allowed for any request
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Write permissions are only allowed to the author of a post
        return obj.user == request.user
    
    
class IsAuthenticatedOrWriteOnly(permissions.BasePermission):
    """
    The request is authenticated as a user, or is a write-only request.
    """

    def has_permission(self, request, view):
        WRITE_METHODS = ["POST", ]

        return (
            request.method in WRITE_METHODS or
            request.user and
            request.user.is_authenticated
        )