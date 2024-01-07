from django import forms
from service_objects.fields import ModelField
from service_objects.services import ServiceWithResult

from models_app.models.like import Like
from models_app.models.photo import Photo
from models_app.models.user import User


class CreateDeleteLikeService(ServiceWithResult):
    id = forms.IntegerField(min_value=1)
    current_user = ModelField(User)

    def process(self):
        self.result = self.like()
        return self

    def like(self):
        try:
            like = Like.objects.get(user=self.user(), photo=self.photo())
            return like.delete()
        except:
            return Like.objects.create(user=self.user(), photo=self.photo())

    def user(self):
        return self.cleaned_data.get('current_user')

    def photo(self):
        return Photo.objects.get(id=self.cleaned_data['id'])
