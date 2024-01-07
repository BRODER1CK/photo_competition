from rest_framework import serializers

from models_app.models.comment import Comment


class CreateCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['text']
