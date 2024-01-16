# django modules
from django.urls import path

# viewsets
from feeds.views import (
    FeedViewSet
)

feed_list = FeedViewSet.as_view({
    'post': 'create',
    'get': 'list'
})

urlpatterns = [
    path('', feed_list),
]