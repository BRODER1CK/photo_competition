import datetime
import json

from decouple import config
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
        current_time = datetime.datetime.now()
        photo_delete_delay = config(
            "PHOTO_DELETE_TIME_SECONDS", default=86400, cast=int
        )
        task = delete_photo.apply_async((photo.id,), countdown=photo_delete_delay)
        task_id = f"celery_delete_task_{photo.id}"
        task_time = current_time + datetime.timedelta(seconds=photo_delete_delay)
        task_dict = {
            "task_id": task.id,
            "task_time": task_time.strftime("%d/%m/%Y_%H:%M:%S"),
        }
        app.backend.set(task_id, json.dumps(task_dict))
        if photo.comments:
            self.process_comments(photo.comments)
        return photo

    def restore_photo(self):
        photo = self.photo()
        photo.status = "M"
        photo.save()
        redis_key = f"celery_delete_task_{photo.id}"
        task = app.backend.get(redis_key)
        task_dict = json.loads(task)
        task_id = task_dict.get("task_id")
        app.control.revoke(task_id, terminate=True)
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
            self.add_error("user", PermissionDenied("You do not have permission"))
            self.response_status = status.HTTP_404_NOT_FOUND
