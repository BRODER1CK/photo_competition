from django import forms
from django.core.exceptions import BadRequest, PermissionDenied
from rest_framework import status
from service_objects.fields import ModelField
from service_objects.services import ServiceWithResult

from models_app.models.comment import Comment
from models_app.models.user import User
from notifications.views import send_notification


class CommentDeleteService(ServiceWithResult):
    id = forms.IntegerField(min_value=1)
    current_user = ModelField(User)
    custom_validations = ["validate_user", "validate_comments"]

    def process(self):
        self.run_custom_validations()
        if self.is_valid():
            self.result = self.delete_comment()
        return self

    def delete_comment(self):
        comment = self.comment()
        parent = comment.content_object
        while parent.__class__.__name__ != "Photo":
            parent = parent.content_object
        comment.delete()
        parent.refresh_from_db()
        send_notification(
            self.user().id,
            f"Пользователь {self.user()} удалил комментарий к Вашей фотографии. "
            f"Количество комментариев: {parent.comment_count}",
        )
        return Comment.objects.none()

    def comment(self):
        return Comment.objects.get(id=self.cleaned_data["id"])

    def user(self):
        return self.cleaned_data.get("current_user")

    def validate_user(self):
        if not self.user() or self.comment().user != self.user():
            self.add_error("user", PermissionDenied("You do not have permission"))
            self.response_status = status.HTTP_403_FORBIDDEN

    def validate_comments(self):
        if self.comment().comments.all():
            self.add_error(
                "user",
                BadRequest(
                    "You can not delete a comment, there are others underneath it"
                ),
            )
            self.response_status = status.HTTP_400_BAD_REQUEST
