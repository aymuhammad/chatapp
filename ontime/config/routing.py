# it set variable of urlpatterns just like you'd normally use in django urls.py
# the config routing in asgi.py would work correctly 

from django.urls import path
from ontime.chatapp.consumers import ChatConsumer

websocket_urlpatterns = [
    path("", ChatConsumer.as_asgi())
]