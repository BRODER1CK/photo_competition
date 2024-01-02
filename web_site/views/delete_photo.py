from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DeleteView

from models_app.models.photo import Photo
from utils.data_mixin import DataMixin


# class DeletePhoto(LoginRequiredMixin, DataMixin, DeleteView):
#     model = Photo
#     template_name = 'web_site/add_photo.html'
#     success_url = reverse_lazy('home')
#     id_url_kwarg = 'photo_id'
#     title_page = 'Удаление фотографии'
#
#     def get_object(self, queryset=None):
#         return get_object_or_404(Photo.objects.all(), id=self.kwargs[self.id_url_kwarg])

class DeletePhoto(LoginRequiredMixin, View):
    def get(self, request, photo_id):
        obj = get_object_or_404(Photo, id=photo_id, user=request.user)
        obj.status = 'D'
        obj.save()

        return redirect('web_site:profile')