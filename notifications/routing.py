from django.urls import path

from .consumers import NotificationsConsumer

websocket_urlpatterns = [
    path("ws/notifications/<int:user_id>/", NotificationsConsumer.as_asgi())
]
