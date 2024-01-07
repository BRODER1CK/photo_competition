from rest_framework import serializers

from models_app.models.comment import Comment


class ListCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
