import secrets

from django.core.exceptions import PermissionDenied
from rest_framework import status
from service_objects.fields import ModelField
from service_objects.services import ServiceWithResult

from models_app.models.user import User


class GenerateTokenService(ServiceWithResult):
    current_user = ModelField(User, required=False)
    custom_validations = ["validate_user"]

    def process(self):
        self.run_custom_validations()
        if self.is_valid():
            self.result = self.token()
        return self

    def token(self):
        current_user = self.cleaned_data.get("current_user")
        current_user.token = secrets.token_hex(16)
        current_user.save()
        return current_user

    def validate_user(self):
        if not self.cleaned_data.get("current_user"):
            self.add_error("user", PermissionDenied(f"You must be logged in"))
            self.response_status = status.HTTP_401_UNAUTHORIZED
