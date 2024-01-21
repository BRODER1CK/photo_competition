from django import forms
from django.contrib.contenttypes.models import ContentType
from service_objects.services import ServiceWithResult

from models_app.models.comment import Comment
from django.apps import apps


class CommentShowService(ServiceWithResult):
    id = forms.IntegerField(min_value=1)

    def process(self):
        self.result = self.comment()
        return self

    def comment(self):
        return Comment.objects.get(id=self.cleaned_data['id'])
