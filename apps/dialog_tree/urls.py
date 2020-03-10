from django.urls import include, path
from rest_framework.routers import SimpleRouter

from apps.users.views import DialogViewSet

router = SimpleRouter()
router.register('dialogs', DialogViewSet, basename='dialog')

urlpatterns = [
    path('', include(router.urls)),
]
