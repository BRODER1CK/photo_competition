from rest_framework import serializers

from models_app.models.photo import Photo


class UpdatePhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ['title', 'description', 'current_photo']
        extra_kwargs = {'description': {'required': True}}


class PartialUpdatePhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ['title', 'description', 'current_photo']
        extra_kwargs = {'title': {'required': False},
                        'current_photo': {'required': False}}
