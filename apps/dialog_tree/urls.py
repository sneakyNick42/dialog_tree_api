"""`dialog_tree` app urls."""
from django.urls import include, path
from rest_framework.routers import SimpleRouter

from . import views

router = SimpleRouter()
router.register('dialogs', views.DialogViewSet, basename='dialog')

urlpatterns = [
    path('', include(router.urls)),
]
