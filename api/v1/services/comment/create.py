from django import forms
from django.contrib.contenttypes.models import ContentType
from service_objects.fields import ModelField
from service_objects.services import ServiceWithResult

from models_app.models.comment import Comment
from models_app.models.user import User
from django.apps import apps


class CommentCreateService(ServiceWithResult):
    text = forms.CharField(max_length=255)
    content_type = forms.ChoiceField(choices=(('Photo', 'Photo'), ('Comment', 'Comment')))
    object_id = forms.IntegerField(min_value=1)
    current_user = ModelField(User)

    def process(self):
        self.result = self.create_comment()
        return self

    def create_comment(self):
        return Comment.objects.create(user=self.cleaned_data['current_user'],
                                      text=self.cleaned_data['text'],
                                      content_type=ContentType.objects.get_for_model(
                                          apps.get_model('models_app',
                                                         self.cleaned_data['content_type'])),
                                      object_id=self.cleaned_data['object_id'])
