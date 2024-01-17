from rest_framework import serializers

from models_app.models.photo import Photo


class ListPhotoSerializer(serializers.ModelSerializer):
    likes_count = serializers.SerializerMethodField()
    comments_count = serializers.SerializerMethodField()
    publication_date = serializers.SerializerMethodField()
    author = serializers.CharField(source='user.username')

    class Meta:
        model = Photo
        fields = ['likes_count', 'comments_count', 'author', 'title', 'publication_date', 'description']

    def get_likes_count(self, obj):
        return obj.likes.count()

    def get_comments_count(self, obj):
        return obj.comments.count()

    def get_publication_date(self, obj):
        return self.format_date(obj.updated_at)

    def format_date(self, date):
        return date.strftime("%d-%m-%Y")
