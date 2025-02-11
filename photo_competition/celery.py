import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "photo_competition.settings")

app = Celery("photo_competition")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
