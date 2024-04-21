from rest_framework import serializers

from models_app.models.photo import Photo


class ListPhotoSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source="user.username")
    publication_date = serializers.SerializerMethodField()

    def get_publication_date(self, obj):
        return self.format_date(obj.updated_at)

    def format_date(self, date):
        return date.strftime("%d-%m-%Y")

    class Meta:
        model = Photo
        fields = [
            "id",
            "status",
            "current_photo",
            "like_count",
            "comment_count",
            "author",
            "title",
            "publication_date",
            "description",
        ]
