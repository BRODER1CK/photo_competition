from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import UpdateView

from models_app.models.photo import Photo
from utils.data_mixin import DataMixin
from web_site.forms.add_photo_form import AddPhotoForm


# class EditPhoto(LoginRequiredMixin, DataMixin, UpdateView):
#     model = Photo
#     fields = ['title', 'description']
#     template_name = 'web_site/add_photo.html'
#     success_url = reverse_lazy('home')
#     id_url_kwarg = 'photo_id'
#     title_page = 'Редактирование фотографии'
#
#     def get_object(self, queryset=None):
#         return get_object_or_404(Photo.objects.all(), id=self.kwargs[self.id_url_kwarg])

class EditPhoto(LoginRequiredMixin, View):
    def get(self, request, photo_id):
        obj = get_object_or_404(Photo, id=photo_id, user=request.user)
        form = AddPhotoForm(instance=obj)

        return render(request, "web_site/add_photo.html",
                      {'form': form, 'title': 'Изменение фотографии'})

    def post(self, request, photo_id):
        obj = get_object_or_404(Photo, id=photo_id, user=request.user)
        form = AddPhotoForm(request.POST, instance=obj)
        if form.is_valid():
            obj.previous_photo = obj.current_photo
            obj.current_photo = request.FILES['current_photo']
            obj.title = request.POST['title']
            obj.description = request.POST['description']
            obj.save()
            return redirect('profile')

        return render(request, "web_site/add_photo.html",
                      {'form': form, 'title': 'Изменение фотографии'})
