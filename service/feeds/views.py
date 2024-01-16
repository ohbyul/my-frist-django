# drf modules
from rest_framework import viewsets 
from rest_framework.response import Response
from rest_framework import status

# models
from feeds.models import (
    Feed
)

# serializer
from feeds.serializers import (
    FeedSerializer
)

# permissions
from feeds.permissions import (
    IsFeedOwnerOrReadOnly
)

# Create your views here.
class FeedViewSet(viewsets.ModelViewSet):
    queryset = Feed.objects.all()
    serializer_class = FeedSerializer
    permission_classes = [ IsFeedOwnerOrReadOnly ]