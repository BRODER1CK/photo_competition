from rest_framework import serializers

from models_app.models.photo import Photo


class PhotoSerializer(serializers.ModelSerializer):
    # user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Photo
        fields = "__all__"
