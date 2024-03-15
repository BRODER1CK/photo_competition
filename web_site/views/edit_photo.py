from django.shortcuts import render
from django.views import View

from api.v1.views.photo import RetrieveUpdateDeletePhotoView


class EditPhoto(View):
    def get(self, request, id):
        photo = RetrieveUpdateDeletePhotoView().get(request, id=id).data
        return render(request, 'web_site/edit_photo.html',
                      {'title': 'Изменение фотографии', 'user': request.user, 'id': photo['id']})
