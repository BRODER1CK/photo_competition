from rest_framework import serializers

from models_app.models.comment import Comment


class ShowCommentSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField()
    content_type = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ['id', 'content_type', 'object_id', 'text', 'comments']

    def get_comments(self, comment):
        comments = comment.comments.all()
        serializer = self.__class__(comments, many=True)
        return serializer.data

    def get_content_type(self, obj):
        return obj.content_type.name
