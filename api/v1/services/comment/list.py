from service_objects.services import ServiceWithResult

from models_app.models.photo import Photo
from models_app.models.comment import Comment


class CommentListService(ServiceWithResult):
    def process(self):
        self.result = self.comments()
        return self

    def comments(self):
        object_id = self.cleaned_data['object_id']
        content_type = self.cleaned_data['content_type']
        if content_type == 'photo':
            photo = Photo.objects.get(id=object_id)
            comments = Comment.objects.filter(content_object=photo)
        elif content_type == 'comment':
            comment = Comment.objects.get(id=object_id)
            comments = Comment.objects.filter(content_object=comment)
        return comments
