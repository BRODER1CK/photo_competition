from rest_framework import serializers

from models_app.models.like import Like


class ListLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['user_id']
