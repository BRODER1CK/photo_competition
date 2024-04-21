from django import forms
from service_objects.services import ServiceWithResult

from models_app.models.like import Like
from models_app.models.photo import Photo


class LikeListService(ServiceWithResult):
    photo_id = forms.IntegerField(min_value=1)

    def process(self):
        self.result = self.likes()
        return self

    def likes(self):
        return Like.objects.filter(
            photo_id=self.cleaned_data["photo_id"]
        ).select_related("user")
