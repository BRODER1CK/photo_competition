from rest_framework import serializers

from models_app.models.comment import Comment


class UpdateCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'text']
