from django.urls import include, path

from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from api.views import CommentViewSet, GroupViewSet, PostViewSet, UserViewSet


router = DefaultRouter()
router.register('users', UserViewSet)
router.register('posts', PostViewSet)
router.register('groups', GroupViewSet)
router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token),
]
