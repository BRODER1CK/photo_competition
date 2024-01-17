from rest_framework import serializers

from models_app.models.comment import Comment


class CreateCommentSerializer(serializers.ModelSerializer):
    content_type = serializers.ChoiceField(choices=(('Photo', 'Photo'), ('Comment', 'Comment')))

    class Meta:
        model = Comment
        fields = ['text', 'content_type', 'object_id']
