from rest_framework import serializers

from models_app.models.like import Like


class ShowLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['user_id', 'photo_id', 'id']
