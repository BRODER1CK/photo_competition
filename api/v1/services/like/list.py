from django import forms
from django.core.paginator import EmptyPage
from service_objects.services import ServiceWithResult

from models_app.models.like import Like
from models_app.models.photo import Photo

class LikeListService(ServiceWithResult):
    id = forms.IntegerField(min_value=1)


    def process(self):
        self.result = self.likes()
        return self

    def likes(self):
        try:
            return Like.objects.filter(photo=self.photo())
        except EmptyPage:
            return Like.objects.none()

    def photo(self):
        return Photo.objects.get(id=self.cleaned_data['id'])
