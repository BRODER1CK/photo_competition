from django.contrib.auth import logout
from django.shortcuts import redirect
from django.views import View


class Logout(View):
    def get(self, request):
        logout(request)
        print(request.META.get('HTTP_REFERER'))
        if request.META.get('HTTP_REFERER') == 'http://127.0.0.1:8000/profile/':
            return redirect('web_site:home')
        else:
            return redirect(request.META.get('HTTP_REFERER'))
