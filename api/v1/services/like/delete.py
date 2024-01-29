from django import forms
from service_objects.fields import ModelField
from service_objects.services import ServiceWithResult

from models_app.models.like import Like
from models_app.models.photo import Photo
from models_app.models.user import User


class LikeDeleteService(ServiceWithResult):
    photo_id = forms.IntegerField(min_value=1)
    current_user = ModelField(User)

    def process(self):
        self.result = self.unlike()
        return self

    def unlike(self):
        like = Like.objects.filter(user=self.cleaned_data['current_user'], photo=self.photo())
        like.delete()
        return Like.objects.none()

    def photo(self):
        return Photo.objects.get(id=self.cleaned_data['photo_id'])
