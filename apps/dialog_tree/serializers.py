"""`dialog_tree` app serializers."""
from rest_framework import serializers

from apps.dialog_tree.models import Dialog


class DialogSerializer(serializers.ModelSerializer):
    """Dialog serializer."""

    owner = serializers.HyperlinkedRelatedField(view_name='user-detail', read_only=True)

    class Meta:
        model = Dialog
        fields = (
            'name', 'owner', 'slug',
            'description', 'finished'
        )
        read_only_fields = ('owner',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.context['view'].action == 'update':
            self.fields['name'].read_only = True
        else:
            self.fields['finished'].read_only = True

    def create(self, validated_data):
        """Setting owner."""
        validated_data['owner'] = self.context['request'].user
        return super().create(validated_data)
