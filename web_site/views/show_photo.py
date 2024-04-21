from django.shortcuts import render
from django.views import View

from api.v1.views.photo import RetrieveUpdateDeletePhotoView


class ShowPhoto(View):
    def get(self, request, id):
        photo = RetrieveUpdateDeletePhotoView().get(request, id=id).data
        return render(
            request, "web_site/show_photo.html", {"photo": photo, "user": request.user}
        )
