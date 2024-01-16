# drf modules
from rest_framework.permissions import BasePermission
from rest_framework.permissions import SAFE_METHODS

class IsFeedOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, feed):
        if request.METHOD in SAFE_METHODS + tuple(['POST']):
            return True
        else: 
            return request.user == feed.user