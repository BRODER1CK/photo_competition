from django import forms
from django.core.exceptions import PermissionDenied
from rest_framework import status
from service_objects.fields import ModelField
from service_objects.services import ServiceWithResult

from models_app.models.photo import Photo
from models_app.models.user import User
from models_app.tasks import delete_photo
from notifications.views import send_notification
from photo_competition.celery import app


class PhotoDeleteService(ServiceWithResult):
    id = forms.IntegerField(min_value=1)
    current_user = ModelField(User)
    custom_validations = ["validate_user"]

    def process(self):
        self.run_custom_validations()
        if self.is_valid():
            if self.photo().status == "D":
                self.result = self.restore_photo()
            else:
                self.result = self.delete_photo()
        return self

    def delete_photo(self):
        photo = self.photo()
        photo.status = "D"
        photo.save()
        redis_key = f"celery_delete_task_{photo.id}"
        result = delete_photo.apply_async((photo.id,), countdown=86400)
        app.backend.set(redis_key, result.id)
        if photo.comments:
            self.process_comments(photo.comments)
        return photo

    def restore_photo(self):
        photo = self.photo()
        photo.status = "M"
        photo.save()
        redis_key = f"celery_delete_task_{photo.id}"
        task_id = app.backend.get(redis_key)
        app.control.revoke(task_id.decode("utf-8"), terminate=True)
        return photo

    def process_comments(self, comments):
        for comment in comments.all():
            send_notification(
                comment.user_id,
                "Фотография, к которой Вы оставили комментарий, отправлена на удаление, "
                "скоро Ваш комментарий будет удален",
            )
            if comment.comments:
                self.process_comments(comment.comments)

    def photo(self):
        return Photo.objects.get(id=self.cleaned_data["id"])

    def user(self):
        return self.cleaned_data.get("current_user")

    def validate_user(self):
        if not self.user() or self.photo().user != self.user():
            self.add_error("user", PermissionDenied(f"You do not have permission"))
            self.response_status = status.HTTP_404_NOT_FOUND
