from rest_framework import serializers

from models_app.models.photo import Photo


class UpdatePhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ['title', 'description', 'current_photo']

class PartialUpdatePhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ['title', 'description', 'current_photo']
        extra_kwargs = {'title': {'required': False},
                        'description': {'required': False},
                        'current_photo': {'required': False}}
