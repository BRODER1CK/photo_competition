from django.shortcuts import get_object_or_404, render
from django.views import View
from models_app.models.photo import Photo


class ShowPhoto(View):
    def get(self, request, photo_id):
        photo = get_object_or_404(Photo, id=photo_id)

        return render(request, 'web_site/photo.html',
                      {'title': photo.title, 'photo': photo})
