from rest_framework import serializers

from models_app.models.photo import Photo


class ShowPhotoSerializer(serializers.ModelSerializer):
    # user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Photo
        fields = "__all__"
