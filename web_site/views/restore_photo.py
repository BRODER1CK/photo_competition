from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from django.views import View
from models_app.models.photo import Photo


class RestorePhoto(LoginRequiredMixin, View):
    def get(self, request, photo_id):
        obj = get_object_or_404(Photo, id=photo_id, user=request.user)
        obj.status = 'M'
        obj.save()

        return redirect('web_site:profile')
