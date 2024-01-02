from django import forms
from django.core.paginator import Paginator, EmptyPage
from service_objects.fields import ModelField
from service_objects.services import ServiceWithResult

from models_app.models.photo import Photo
from models_app.models.user import User
from photo_competition.settings.drf import REST_FRAMEWORK


class PhotoListService(ServiceWithResult):
    page = forms.IntegerField(required=False)
    per_page = forms.IntegerField(required=False)
    current_user = ModelField(User, required=False)

    def process(self):
        self.result = self.photos()
        return self

    def photos(self):
        try:
            if self.cleaned_data.get('current_user') and self.cleaned_data.get('current_user').is_superuser:
                return Paginator(
                    Photo.objects.all(),
                    self.cleaned_data["per_page"] or REST_FRAMEWORK["PAGE_SIZE"],
                ).page(self.cleaned_data["page"] or 1)
            elif self.cleaned_data.get('current_user'):
                return Paginator(
                    Photo.published.all() | Photo.objects.filter(user=self.cleaned_data.get('current_user')),
                    self.cleaned_data["per_page"] or REST_FRAMEWORK["PAGE_SIZE"],
                ).page(self.cleaned_data["page"] or 1)
            else:
                return Paginator(
                    Photo.published.all(),
                    self.cleaned_data["per_page"] or REST_FRAMEWORK["PAGE_SIZE"],
                ).page(self.cleaned_data["page"] or 1)
        except EmptyPage:
            return Paginator(
                Photo.objects.none(),
                self.cleaned_data["per_page"] or REST_FRAMEWORK["PAGE_SIZE"],
            ).page(1)
