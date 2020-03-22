"""`dialog_tree` app serializers."""
from rest_framework import serializers

from apps.dialog_tree.models import Answer, Dialog, Question


class AnswerSerializer(serializers.ModelSerializer):
    """Answer serializer."""

    question = serializers.PrimaryKeyRelatedField(queryset=Question.objects.all())
    next_question = serializers.HyperlinkedRelatedField(view_name='question-detail', read_only=True)

    class Meta:
        model = Answer
        fields = (
            'id', 'text', 'question',
            'next_question'
        )


class AnswerUpdateSerializer(AnswerSerializer):
    """Answer update serializer."""

    question = serializers.PrimaryKeyRelatedField(read_only=True)
    next_question = serializers.PrimaryKeyRelatedField(queryset=Question.objects.all())

    class Meta(AnswerSerializer.Meta):
        fields = (
            'id', 'text', 'next_question'
        )


class QuestionSerializer(serializers.ModelSerializer):
    """Question serializer."""

    answers = AnswerSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = (
            'id', 'text', 'answers'
        )


class DialogSerializer(serializers.ModelSerializer):
    """Dialog serializer."""

    owner = serializers.HyperlinkedRelatedField(view_name='user-detail', read_only=True)
    first_question = serializers.HyperlinkedRelatedField(view_name='question-detail', read_only=True)

    class Meta:
        model = Dialog
        fields = (
            'slug', 'name', 'owner',
            'description', 'finished', 'first_question'
        )
        read_only_fields = ('owner', 'finished',)

    def create(self, validated_data):
        """Setting owner."""
        validated_data['owner'] = self.context['request'].user
        return super().create(validated_data)


class DialogUpdateSerializer(DialogSerializer):
    """Dialog update serializer."""

    first_question = serializers.PrimaryKeyRelatedField(queryset=Question.objects.all())

    class Meta(DialogSerializer.Meta):
        fields = (
            'slug', 'description', 'finished',
            'first_question'
        )
