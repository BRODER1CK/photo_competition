from celery.schedules import crontab

CELERY_BROKER_URL = "redis://localhost:6379/0"
CELERY_RESULT_BACKEND = "redis://localhost:6379/0"
CELERY_ACCEPT_CONTENT = ["json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"
CELERY_TIMEZONE = "Europe/Moscow"
CELERY_BEAT_SCHEDULE = {
    "delete_photos_at_3_am": {
        "task": "models_app.tasks.delete_photos_at_3_am",
        "schedule": crontab(hour=3, minute=0),
    },
}
