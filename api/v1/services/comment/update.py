from django import forms
from django.core.exceptions import PermissionDenied
from rest_framework import status
from service_objects.fields import ModelField
from service_objects.services import ServiceWithResult

from models_app.models.comment import Comment
from models_app.models.user import User


class CommentUpdateService(ServiceWithResult):
    text = forms.CharField(max_length=255)
    id = forms.IntegerField(min_value=1)
    current_user = ModelField(User)
    custom_validations = ["validate_user"]

    def process(self):
        self.run_custom_validations()
        if self.is_valid():
            self.result = self.update_comment()
        return self

    def update_comment(self):
        comment = self.comment()
        if self.cleaned_data.get("text"):
            comment.text = self.cleaned_data["text"]
        comment.save()
        return comment

    def comment(self):
        return Comment.objects.get(id=self.cleaned_data["id"])

    def user(self):
        return self.cleaned_data.get("current_user")

    def validate_user(self):
        if not self.user() or self.comment().user != self.user():
            self.add_error("user", PermissionDenied("You do not have permission"))
            self.response_status = status.HTTP_403_FORBIDDEN
