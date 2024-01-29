from rest_framework import serializers

from models_app.models.user import User


class GenerateTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['token']
