"""`dialog_tree` app views."""
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from apps.dialog_tree.models import Answer, Dialog, Question
from apps.dialog_tree.permissions import IsOwnerOrReadOnly
from apps.dialog_tree.serializers import AnswerSerializer, DialogSerializer, QuestionSerializer


class DialogViewSet(ModelViewSet):
    """
    list:
    List of dialogs.
    retrieve:
    Return the given dialog.
    create:
    Create a new dialog instance.
    """

    serializer_class = DialogSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    queryset = Dialog.objects.all()
    lookup_field = 'slug'
    filter_fields = ('owner',)


class QuestionViewSet(ModelViewSet):
    """
    list:
    List of questions.
    retrieve:
    Return the given question.
    create:
    Create a new question instance.
    """

    serializer_class = QuestionSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Question.objects.all()


class AnswerViewSet(ModelViewSet):
    """
    list:
    List of answers.
    retrieve:
    Return the given answer.
    create:
    Create a new answer instance.
    """

    serializer_class = AnswerSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Answer.objects.all()
