from rest_framework import serializers

from models_app.models.comment import Comment


class ShowCommentSerializer(serializers.ModelSerializer):
    content_type = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()

    def get_content_type(self, obj):
        return obj.content_type.name

    def get_user(self, obj):
        return obj.user.username

    def get_comments(self, comment):
        serializer = self.__class__(
            comment.comments.select_related('user', 'content_type'), many=True)
        return serializer.data

    class Meta:
        model = Comment
        fields = ['id', 'content_type', 'object_id', 'user', 'text', 'comments']
