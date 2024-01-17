from django.contrib.auth import logout
from django.shortcuts import redirect
from django.views import View
from decouple import config


class Logout(View):
    def get(self, request):
        logout(request)
        if request.META.get('HTTP_REFERER') == f'{config('SCHEMA')}://{config('DOMAIN')}/profile/':
            return redirect('web_site:home')
        else:
            return redirect(request.META.get('HTTP_REFERER'))
