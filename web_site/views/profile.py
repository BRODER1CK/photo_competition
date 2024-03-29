from django.shortcuts import render
from django.views import View

from photo_competition.settings.authentication import DEFAULT_USER_IMAGE


class Profile(View):
    def get(self, request):
        return render(request, 'web_site/profile.html',
                      {'title': 'Профиль', 'profile': request.user,
                       'default_image': DEFAULT_USER_IMAGE})
