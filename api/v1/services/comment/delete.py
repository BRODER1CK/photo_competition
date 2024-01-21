from django import forms
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import PermissionDenied
from rest_framework import status
from service_objects.fields import ModelField
from service_objects.services import ServiceWithResult

from models_app.models.comment import Comment
from models_app.models.user import User


class CommentDeleteService(ServiceWithResult):
    id = forms.IntegerField(min_value=1)
    current_user = ModelField(User)

    def process(self):
        self.run_custom_validations()
        if self.is_valid():
            self.result = self.delete_comment()
        return self

    def delete_comment(self):
        comment = self.comment()
        return comment.delete()

    def comment(self):
        return Comment.objects.get(id=self.cleaned_data['id'])

    def user(self):
        return self.cleaned_data.get('current_user')

    def validate_user(self):
        if not self.user() or self.comment().user != self.user():
            self.add_error('user', PermissionDenied(f'You do not have permission'))
            self.response_status = status.HTTP_404_NOT_FOUND
