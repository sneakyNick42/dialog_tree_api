"""`dialog_tree` app views."""
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from apps.dialog_tree.models import Dialog
from apps.dialog_tree.permissions import IsOwnerOrReadOnly
from apps.dialog_tree.serializers import DialogSerializer


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
