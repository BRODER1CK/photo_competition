from django import forms
from django.core.exceptions import PermissionDenied
from rest_framework import status
from service_objects.fields import ModelField
from service_objects.services import ServiceWithResult

from models_app.models.photo import Photo
from models_app.models.user import User


class PhotoUpdateService(ServiceWithResult):
    id = forms.IntegerField(min_value=1)
    title = forms.CharField(max_length=255)
    description = forms.CharField()
    current_photo = forms.ImageField()
    current_user = ModelField(User)
    custom_validations = ['validate_user']

    def process(self):
        self.run_custom_validations()
        if self.is_valid():
            self.result = self.update_photo()
        return self

    def update_photo(self):
        photo = self.photo()
        if self.cleaned_data.get('title'):
            photo.title = self.cleaned_data['title']
        if self.cleaned_data.get('description'):
            photo.description = self.cleaned_data['description']
        if self.cleaned_data.get('current_photo'):
            photo.previous_photo = photo.current_photo
            photo.current_photo = self.cleaned_data['current_photo']
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


class PhotoPartialUpdateService(PhotoUpdateService):
    title = forms.CharField(required=False, max_length=255)
    description = forms.CharField(required=False)
    current_photo = forms.ImageField(required=False)
