from rest_framework import serializers

from models_app.models.photo import Photo


class CreatePhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ['title', 'description', 'current_photo']
