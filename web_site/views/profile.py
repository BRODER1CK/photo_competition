from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import UpdateView

from models_app.models.photo import Photo
from models_app.models.user import User
from web_site.forms.profile import ProfileForm
from photo_competition.settings.authentication import DEFAULT_USER_IMAGE


# class Profile(LoginRequiredMixin, UpdateView):
#     model = get_user_model()
#     form_class = ProfileForm
#     template_name = 'web_site/profile.html'
#     # extra_context = {
#     #     'title': 'Личный кабинет',
#     #     'default_image': DEFAULT_USER_IMAGE,
#     #     'photos': Photo.objects.all()
#     # }
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'Личный кабинет'
#         context['default_image']: DEFAULT_USER_IMAGE
#         context['photos'] = Photo.objects.filter(user_id=self.request.user)
#         return context
#
#     def get_success_url(self):
#         return reverse_lazy('profile')
#
#     def get_object(self, queryset=None):
#         return self.request.user

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
