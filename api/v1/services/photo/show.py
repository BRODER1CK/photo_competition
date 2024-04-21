from django import forms
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from service_objects.fields import ModelField
from service_objects.services import ServiceWithResult

from models_app.models.photo import Photo
from models_app.models.user import User


class PhotoShowService(ServiceWithResult):
    id = forms.IntegerField(min_value=1)
    current_user = ModelField(User, required=False)
    custom_validations = ["validate_user"]

    def process(self):
        self.run_custom_validations()
        if self.is_valid():
            self.result = self.photo()
        return self

    def photo(self):
        return Photo.objects.get(id=self.cleaned_data["id"])

    def user(self):
        return self.cleaned_data.get("current_user")

    def validate_user(self):
        if (
            self.user()
            and not self.user().is_superuser
            and self.photo().status != "P"
            and self.photo().user != self.user()
        ):
            self.add_error(
                "id",
                ObjectDoesNotExist(
                    f'Photo with id = {self.cleaned_data["id"]} does not exist'
                ),
            )
            self.response_status = status.HTTP_404_NOT_FOUND
        elif not self.user() and self.photo().status != "P":
            self.add_error(
                "id",
                ObjectDoesNotExist(
                    f'Photo with id = {self.cleaned_data["id"]} does not exist'
                ),
            )
            self.response_status = status.HTTP_404_NOT_FOUND
