"""`dialog_tree` app urls."""
from django.urls import include, path
from rest_framework.routers import SimpleRouter
from rest_framework_nested import routers

from . import views

router = SimpleRouter()
router.register('dialogs', views.DialogViewSet, basename='dialog')

dialogs_router = routers.NestedSimpleRouter(router, 'dialogs', lookup='dialog')
dialogs_router.register('questions', views.QuestionViewSet, basename='dialog-questions')
dialogs_router.register('answers', views.AnswerViewSet, basename='dialog-answers')

# router.register('questions', views.QuestionViewSet, basename='question')
# router.register('answers', views.AnswerViewSet, basename='answer')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(dialogs_router.urls)),
]
