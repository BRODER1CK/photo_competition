from rest_framework import serializers

from models_app.models.like import Like


class ShowLikeSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    class Meta:
        model = Like
        fields = ['user', 'photo_id', 'id']

    def get_user(self, obj):
        return obj.user.username
