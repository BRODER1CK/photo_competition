from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.views import View
from models_app.models.photo import Photo


class DeletePhoto(LoginRequiredMixin, View):
    def get(self, request, photo_id):
        obj = get_object_or_404(Photo, id=photo_id, user=request.user)
        obj.status = 'D'
        obj.save()

        return redirect('web_site:profile')
