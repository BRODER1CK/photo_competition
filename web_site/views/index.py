from decouple import config
from django.shortcuts import render
from django.views.generic import View


class Index(View):
    def get(self, request):
        return render(
            request,
            "web_site/index.html",
            {
                "user": request.user,
                "schema": config("SCHEMA"),
                "domain": config("DOMAIN"),
            },
        )
