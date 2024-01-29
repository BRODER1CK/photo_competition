from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from web_site.forms.add_photo_form import AddPhotoForm


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

            return redirect('web_site:profile')

        return render(request, 'web_site/add_photo.html',
                      {'title': 'Добавление фотографии', 'form': form})
