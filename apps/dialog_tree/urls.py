"""`dialog_tree` app urls."""
from django.urls import include, path
from rest_framework.routers import SimpleRouter

from . import views

router = SimpleRouter()
router.register('dialogs', views.DialogViewSet, basename='dialog')
router.register('answers', views.AnswerViewSet, basename='answer')
router.register('questions', views.QuestionViewSet, basename='question')
router.register('self-questions', views.SelfQuestionViewSet, basename='self-question')

# dialogs_router = routers.NestedSimpleRouter(router, 'dialogs', lookup='dialog')

# router.register('questions', views.QuestionViewSet, basename='question')
# router.register('answers', views.AnswerViewSet, basename='answer')

urlpatterns = [
    path('', include(router.urls)),
    # path('', include(dialogs_router.urls)),
]
