"""`users` app urls."""
from django.urls import include, path
from rest_framework.routers import SimpleRouter

from apps.users.views import UserViewSet

router = SimpleRouter()
router.register('users', UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
]
