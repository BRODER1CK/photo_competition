from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from models_app.models.photo import Photo
from models_app.models.user import User
from web_site.forms.profile import ProfileForm
from photo_competition.settings.authentication import DEFAULT_USER_IMAGE


class Profile(LoginRequiredMixin, View):
    def get(self, request):
        obj = get_object_or_404(User, id=request.user.id)
        form = ProfileForm(instance=obj)

        return render(request, "web_site/profile.html",
                      {'form': form, 'title': 'Личный кабинет',
                       'photos': Photo.objects.filter(user=request.user),
                       'default_image': DEFAULT_USER_IMAGE})

    def post(self, request):
        obj = get_object_or_404(User, id=request.user.id)
        form = ProfileForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('web_site:profile')

        return render(request, "web_site/profile.html",
                      {'form': form, 'title': 'Личный кабинет',
                       'photos': Photo.objects.filter(user=request.user),
                       'default_image': DEFAULT_USER_IMAGE})
