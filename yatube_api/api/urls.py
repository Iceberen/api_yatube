from django.urls import include, path

from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from api.views import CommentViewSet, GroupViewSet, PostViewSet, UserViewSet


v1_router_api = DefaultRouter()
v1_router_api.register('users', UserViewSet)
v1_router_api.register('posts', PostViewSet)
v1_router_api.register('groups', GroupViewSet)
v1_router_api.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)

urlpatterns = [
    path('v1/', include(v1_router_api.urls)),
    path('v1/api-token-auth/', views.obtain_auth_token),
]
