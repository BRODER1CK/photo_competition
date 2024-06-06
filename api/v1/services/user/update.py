from django import forms
from django.core.exceptions import PermissionDenied
from rest_framework import status
from service_objects.fields import ModelField
from service_objects.services import ServiceWithResult

from models_app.models.user import User


class UserUpdateService(ServiceWithResult):
    current_user = ModelField(User)
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)

    def process(self):
        self.run_custom_validations()
        if self.is_valid():
            self.result = self.update_user()
        return self

    def update_user(self):
        user = self.user()
        if self.cleaned_data.get("first_name"):
            user.first_name = self.cleaned_data["first_name"]
        if self.cleaned_data.get("last_name"):
            user.last_name = self.cleaned_data["last_name"]
        user.save()
        return user

    def user(self):
        return self.cleaned_data.get("current_user")

    def validate_user(self):
        if not self.user():
            self.add_error("user", PermissionDenied("You must be logged in"))
            self.response_status = status.HTTP_403_FORBIDDEN


class UserPartialUpdateService(UserUpdateService):
    first_name = forms.CharField(max_length=255, required=False)
    last_name = forms.CharField(max_length=255, required=False)
