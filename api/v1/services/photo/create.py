from django import forms
from service_objects.fields import ModelField
from service_objects.services import ServiceWithResult

from models_app.models.photo import Photo
from models_app.models.user import User


class PhotoCreateService(ServiceWithResult):
    title = forms.CharField(max_length=255)
    description = forms.CharField(required=False)
    current_photo = forms.ImageField()
    current_user = ModelField(User)

    def process(self):
        self.result = self.create_photo()
        return self

    def create_photo(self):
        return Photo.objects.create(
            title=self.cleaned_data["title"],
            description=self.cleaned_data.get("description"),
            current_photo=self.cleaned_data["current_photo"],
            user=self.cleaned_data["current_user"],
        )
