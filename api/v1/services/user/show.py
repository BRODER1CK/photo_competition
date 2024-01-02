from django.core.exceptions import PermissionDenied
from rest_framework import status
from service_objects.fields import ModelField
from service_objects.services import ServiceWithResult

from models_app.models.user import User


class UserShowService(ServiceWithResult):
    current_user = ModelField(User, required=False)

    custom_validations = ['validate_user']

    def process(self):
        self.run_custom_validations()
        if self.is_valid():
            self.result = self.user()
        return self


    def user(self):
        return self.cleaned_data.get('current_user')

    def validate_user(self):
        if not self.user():
            self.add_error('user', PermissionDenied(f'You must be logged in'))
            self.response_status = status.HTTP_404_NOT_FOUND

