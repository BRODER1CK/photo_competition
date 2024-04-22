from django import forms
from django.core.exceptions import ValidationError
from rest_framework import status
from service_objects.fields import ModelField
from service_objects.services import ServiceWithResult

from models_app.models.like import Like
from models_app.models.photo import Photo
from models_app.models.user import User
from notifications.views import send_notification


class LikeCreateService(ServiceWithResult):
    photo_id = forms.IntegerField(min_value=1)
    current_user = ModelField(User)
    custom_validations = ["validate_like"]

    def process(self):
        self.run_custom_validations()
        if self.is_valid():
            self.result = self.like()
        return self

    def like(self):
        like = Like.objects.create(user=self.user(), photo=self.photo())
        send_notification(
            self.user().id,
            f"Пользователь {self.user()} проголосовал за Вашу фотографию. "
            f"Количество голосов: {self.photo().like_count}",
        )
        return like

    def user(self):
        return self.cleaned_data.get("current_user")

    def photo(self):
        return Photo.objects.get(id=self.cleaned_data["photo_id"])

    def validate_like(self):
        if Like.objects.filter(user=self.user(), photo=self.photo()):
            self.add_error("like", ValidationError("Like already exists"))
            self.response_status = status.HTTP_400_BAD_REQUEST
