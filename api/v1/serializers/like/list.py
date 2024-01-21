from rest_framework import serializers

from models_app.models.like import Like


class ListLikeSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    class Meta:
        model = Like
        fields = ['user']

    def get_user(self, obj):
        return obj.user.username
