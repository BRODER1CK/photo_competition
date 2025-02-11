import json
from datetime import datetime

from celery import shared_task

from models_app.models.photo import Photo
from photo_competition.celery import app


@shared_task
def delete_photo(photo_id):
    try:
        photo = Photo.objects.get(id=photo_id)
        if photo.status == "D":
            photo.delete()
    except Photo.DoesNotExist:
        pass


@shared_task
def delete_photos_at_3_am():
    for photo in Photo.objects.filter(status="D"):
        redis_key = f"celery_delete_task_{photo.id}"
        task = app.backend.get(redis_key)
        task_dict = json.loads(task)
        task_time = datetime.strptime(task_dict.get("task_time"), "%d/%m/%Y_%H:%M:%S")
        current_time = datetime.now()
        if current_time > task_time:
            photo.delete()
