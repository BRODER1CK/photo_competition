from django import forms
from django.core.exceptions import PermissionDenied
from rest_framework import status
from service_objects.fields import ModelField
from service_objects.services import ServiceWithResult

from models_app.models.photo import Photo
from models_app.models.user import User


class PhotoDeleteService(ServiceWithResult):
    id = forms.IntegerField(min_value=1)
    current_user = ModelField(User)
    custom_validations = ['validate_user']

    def process(self):
        self.run_custom_validations()
        if self.is_valid():
            if self.photo().status == 'D':
                self.result = self.restore_photo()
            else:
                self.result = self.delete_photo()
        return self

    def delete_photo(self):
        photo = self.photo()
        photo.status = 'D'
        photo.save()
        return photo

    def restore_photo(self):
        photo = self.photo()
        photo.status = 'M'
        photo.save()
        return photo

    def photo(self):
        return Photo.objects.get(id=self.cleaned_data['id'])

    def user(self):
        return self.cleaned_data.get('current_user')

    def validate_user(self):
        if not self.user() or self.photo().user != self.user():
            self.add_error('user', PermissionDenied(f'You do not have permission'))
            self.response_status = status.HTTP_404_NOT_FOUND
