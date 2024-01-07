from django import forms
from service_objects.fields import ModelField
from service_objects.services import ServiceWithResult

from models_app.models.comment import Comment
from models_app.models.photo import Photo
from models_app.models.user import User


class CommentCreateService(ServiceWithResult):
    text = forms.CharField(max_length=255)
    current_user = ModelField(User)

    def process(self):
        self.result = self.create_comment()
        return self

    def create_comment(self):
        text = self.cleaned_data['text']
        content_type = self.cleaned_data['content_type']
        object_id = self.cleaned_data['object_id']
        user = self.cleaned_data['current_user']
        if content_type == 'photo':
            photo = Photo.objects.get(id=object_id)
            comment = Comment.objects.create(user=user, text=text, content_object=photo)
        elif content_type == 'comment':
            parent_comment = Comment.objects.get(id=object_id)
            comment = Comment.objects.create(user=user, text=text, content_object=parent_comment)
        return comment
