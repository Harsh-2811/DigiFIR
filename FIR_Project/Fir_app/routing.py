from django.conf.urls import url
from django.urls import re_path

from . import consumer


websocket_urlpatterns = [

    url(r'ws/fir_app/(?P<room_name>\w+)/$', consumer.ChatConsumer.as_asgi()),

]