from django import forms
from service_objects.services import ServiceWithResult

from models_app.models.comment import Comment


class CommentShowService(ServiceWithResult):
    id = forms.IntegerField(min_value=1)

    def process(self):
        self.result = self.comment()
        return self

    def comment(self):
        return Comment.objects.get(id=self.cleaned_data['id'])
