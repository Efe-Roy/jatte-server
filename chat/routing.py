from django.urls import path

from . import consumers


websocket_urlpatterns = [
    path('ws/<str:room_name>/', consumers.ChatConsumer.as_asgi()),
    path('ws/chat/<str:room_name>/', consumers.NotificationConsumer.as_asgi()),
]