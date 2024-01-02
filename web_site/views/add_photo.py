from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse_lazy
from django.views.generic import CreateView

from utils.data_mixin import DataMixin
from web_site.forms.add_photo_form import AddPhotoForm


# class AddPhoto(LoginRequiredMixin, DataMixin, CreateView):
#     form_class = AddPhotoForm
#     template_name = 'web_site/add_photo.html'
#     title_page = 'Добавление фотографии'
#     success_url = reverse_lazy('home')
#
#     def form_valid(self, form):
#         w = form.save(commit=False)
#         w.user = self.request.user
#         return super().form_valid(form)

class AddPhoto(LoginRequiredMixin, View):
    def get(self, request):
        form = AddPhotoForm()

        return render(request, 'web_site/add_photo.html',
                      {'title': 'Добавление фотографии', 'form': form})

    def post(self, request):
        form = AddPhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.user = self.request.user
            photo.save()

            return redirect('profile')

        return render(request, 'web_site/add_photo.html',
                      {'title': 'Добавление фотографии', 'form': form})