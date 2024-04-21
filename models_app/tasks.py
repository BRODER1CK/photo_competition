from datetime import datetime

from celery import shared_task

from models_app.models.photo import Photo


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
    for photo in Photo.objects.all():
        if (
            photo.status == "D"
            and (datetime.now() - photo.updated_at).total_seconds() > 86400
        ):
            photo.delete()
