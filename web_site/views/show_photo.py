from django.shortcuts import get_object_or_404, render
from django.views import View
from django.views.generic import DetailView

from models_app.models.photo import Photo
from utils.data_mixin import DataMixin


# class ShowPhoto(DataMixin, DetailView):
#     template_name = 'web_site/photo.html'
#     id_url_kwarg = 'photo_id'
#     context_object_name = 'photo'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         return self.get_mixin_context(context, title=context['photo'].title)
#
#     def get_object(self, queryset=None):
#         return get_object_or_404(Photo.published, id=self.kwargs[self.id_url_kwarg])

class ShowPhoto(View):
    def get(self, request, photo_id):
        photo = get_object_or_404(Photo, id=photo_id)

        return render(request, 'web_site/photo.html',
                      {'title': photo.title, 'photo': photo})
