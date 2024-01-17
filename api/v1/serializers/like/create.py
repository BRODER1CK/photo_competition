from rest_framework import serializers

from models_app.models.like import Like


class CreateLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = "__all__"
