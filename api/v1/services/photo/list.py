from django import forms
from django.core.paginator import Paginator, EmptyPage
from django.db.models import Q
from service_objects.fields import ModelField
from service_objects.services import ServiceWithResult

from models_app.models.photo import Photo
from models_app.models.user import User
from photo_competition.settings.drf import REST_FRAMEWORK


class PhotoListService(ServiceWithResult):
    page = forms.IntegerField(required=False)
    per_page = forms.IntegerField(required=False)
    ordering = forms.ChoiceField(choices=(('like_count', 'like_count'),
                                          ('updated_at', 'updated_at'),
                                          ('comment_count', 'comment_count')), required=False)
    ordering_direction = forms.ChoiceField(choices=(('asc', 'asc'), ('desc', 'desc')), required=False)
    search = forms.CharField(required=False, min_length=3)
    current_user = ModelField(User, required=False)

    def process(self):
        self.result = self.photos()
        return self

    def photos(self):
        try:
            return Paginator(
                self.filtered_photos(),
                self.cleaned_data["per_page"] or REST_FRAMEWORK["PAGE_SIZE"],
            ).page(self.cleaned_data["page"] or 1)
        except EmptyPage:
            return Paginator(
                Photo.objects.none(),
                self.cleaned_data["per_page"] or REST_FRAMEWORK["PAGE_SIZE"],
            ).page(1)

    def user(self):
        return self.cleaned_data.get('current_user')

    def filtered_photos(self):
        photos = Photo.objects.all()
        ordering = 'updated_at'
        ordering_direction = 'desc'
        search = self.cleaned_data.get('search')
        if search:
            photos = photos.filter(Q(user__username__icontains=search) |
                                   Q(title__icontains=search) |
                                   Q(description__icontains=search))
        if self.cleaned_data.get('ordering'):
            ordering = self.cleaned_data['ordering']
        if self.cleaned_data.get('ordering_direction'):
            ordering_direction = self.cleaned_data['ordering_direction']
        if ordering_direction == 'desc':
            ordering = '-' + ordering
        if not self.user():
            photos = photos.filter(status='P')
        elif self.user() and not self.user().is_superuser:
            photos = photos.filter(Q(status='P') | Q(user=self.user()))
        return photos.order_by(ordering)
