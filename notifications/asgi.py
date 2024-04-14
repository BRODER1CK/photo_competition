from channels.auth import AuthMiddlewareStack
from channels.routing import URLRouter, ProtocolTypeRouter
from django.core.asgi import get_asgi_application
from routing import websocket_urlpatterns

asgi = get_asgi_application()

application = ProtocolTypeRouter({
    "http": asgi,
    'websocket': AuthMiddlewareStack(
        URLRouter(
        websocket_urlpatterns
        )
    )
})
