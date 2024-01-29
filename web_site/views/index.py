from django.shortcuts import render
from django.views.generic import View
from models_app.models.photo import Photo


class Index(View):
    def get(self, request):

        return render(request,
                      'web_site/index.html',
                      {'title': 'Главная страница',
                       'photos': Photo.published.all()})
