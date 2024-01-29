from django import forms
from django.contrib.contenttypes.models import ContentType
from service_objects.services import ServiceWithResult

from models_app.models.comment import Comment
from django.apps import apps


class CommentListService(ServiceWithResult):
    content_type = forms.ChoiceField(choices=(('Photo', 'Photo'), ('Comment', 'Comment')))
    object_id = forms.IntegerField(min_value=1)

    def process(self):
        self.result = self.comments()
        return self

    def comments(self):
        content_type_id = ContentType.objects.get_for_model(
            apps.get_model('models_app', self.cleaned_data['content_type'])).id
        return (Comment.objects.filter(object_id=self.cleaned_data['object_id'],
                                       content_type_id=content_type_id)
                .prefetch_related('comments')
                .select_related('user', 'content_type'))
