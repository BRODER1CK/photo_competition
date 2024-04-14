from django import forms
from service_objects.fields import ModelField
from service_objects.services import ServiceWithResult

from models_app.models.like import Like
from models_app.models.photo import Photo
from models_app.models.user import User
from notifications.views import send_notification


class LikeDeleteService(ServiceWithResult):
    photo_id = forms.IntegerField(min_value=1)
    current_user = ModelField(User)

    def process(self):
        self.result = self.unlike()
        return self

    def unlike(self):
        like = Like.objects.filter(user=self.user(), photo=self.photo())
        like.delete()
        send_notification(self.user().id,
                          f'Пользователь {self.user()} снял голос с Вашей фотографии. Количество голосов: {self.photo().like_count}')
        return Like.objects.none()

    def user(self):
        return self.cleaned_data.get('current_user')

    def photo(self):
        return Photo.objects.get(id=self.cleaned_data['photo_id'])
