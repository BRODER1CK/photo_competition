from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, View

from models_app.models.photo import Photo
from models_app.models.user import User
from utils.data_mixin import DataMixin


# class Index(DataMixin, ListView):
#     template_name = 'web_site/index.html'
#     context_object_name = 'photos'
#     title_page = 'Главная страница'
#
#     def get_queryset(self):
#         return Photo.published.all()

class Index(View):
    def get(self, request):

        return render(request,
                      'web_site/index.html',
                      {'title': 'Главная страница',
                       'photos': Photo.published.all()})
