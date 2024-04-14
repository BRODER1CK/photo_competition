from django.shortcuts import render
from django.views import View


class AddPhoto(View):
    def get(self, request):
        return render(request, 'web_site/add_photo.html',
                      {'user': request.user})
