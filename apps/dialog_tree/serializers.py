"""`dialog_tree` app serializers."""
from rest_framework import serializers

from apps.dialog_tree.models import Answer, Dialog, Question


class DialogSerializer(serializers.ModelSerializer):
    """Dialog serializer."""

    owner = serializers.HyperlinkedRelatedField(view_name='user-detail', read_only=True)
    questions = serializers.HyperlinkedRelatedField(many=True, view_name='question-detail', read_only=True)

    class Meta:
        model = Dialog
        fields = (
            'name', 'owner', 'slug',
            'description', 'finished', 'questions'
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


class AnswerSerializer(serializers.ModelSerializer):
    """Answer serializer."""

    question = serializers.PrimaryKeyRelatedField(queryset=Question.objects.all())
    next_question = serializers.HyperlinkedRelatedField(view_name='dialog-question-detail', read_only=True)

    class Meta:
        model = Answer
        fields = (
            'text', 'question', 'end',
            'next_question'
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.context.get('view') and self.context['view'].action != 'update':
            self.fields['next_question'].read_only = True


class QuestionSerializer(serializers.ModelSerializer):
    """Question serializer."""

    answers = AnswerSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = (
            'text', 'answers'
        )
