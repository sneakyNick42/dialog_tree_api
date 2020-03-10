from rest_framework import serializers

from apps.dialog_tree.models import Dialog


class DialogSerializer(serializers.ModelSerializer):
    """Dialog serializer."""

    class Meta:
        model = Dialog
        fields = (
            'name', 'owner', 'slug'
        )
        read_only_fields = ('owner',)

    def create(self, validated_data):
        validated_data['owner'] = self.context['request'].user
        return super().create(validated_data)

