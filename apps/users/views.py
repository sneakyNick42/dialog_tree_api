from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet
from rest_framework.viewsets import mixins

from apps.dialog_tree.models import Dialog
from apps.dialog_tree.serializers import DialogSerializer
from apps.users.serializers import UserSerializer


class UserViewSet(mixins.RetrieveModelMixin,
                  mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  GenericViewSet):
    """
    list:
    List of all users.
    retrieve:
    Return the given user.
    create:
    Create a new user instance.
    """

    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()


class DialogViewSet(mixins.RetrieveModelMixin,
                    mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    mixins.DestroyModelMixin,
                    GenericViewSet):
    """
    list:
    List of dialogs.
    retrieve:
    Return the given dialog.
    create:
    Create a new dialog instance.
    """

    serializer_class = DialogSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Dialog.objects.all()
    lookup_field = 'slug'
