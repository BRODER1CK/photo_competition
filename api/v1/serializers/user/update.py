from rest_framework import serializers

from models_app.models.user import User


class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']

class PartialUpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']
        extra_kwargs = {'first_name': {'required': False},
                        'last_name': {'required': False}}
