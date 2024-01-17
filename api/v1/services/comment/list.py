from django import forms
from django.contrib.contenttypes.models import ContentType
from service_objects.services import ServiceWithResult

from models_app.models.comment import Comment
from django.apps import apps


class CommentListService(ServiceWithResult):
    content_type = forms.ChoiceField(choices=(('Photo', 'Photo'), ('Comment', 'Comment')), required=False)
    object_id = forms.IntegerField(min_value=1)

    def process(self):
        self.result = self.comments()
        return self

    def comments(self):
        if self.cleaned_data['content_type']:
            return Comment.objects.filter(object_id=self.cleaned_data['object_id'],
                                      content_type=ContentType.objects.get_for_model(
                                          apps.get_model('models_app',
                                                         self.cleaned_data['content_type'])))
        else:
            return Comment.objects.filter(object_id=self.cleaned_data['object_id'])
