import json
from asgiref.sync import async_to_sync, sync_to_async
from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
from .models import Alerts
from django.contrib.auth import get_user_model
from channels.db import database_sync_to_async
from django.core import serializers

class ChatConsumer(AsyncWebsocketConsumer):


    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )



    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        if text_data_json['code'] == 'new_message':
            latitude = text_data_json['latitude']
            longitude = text_data_json['longitude']
            username = text_data_json['username']


            self.latitude = latitude
            self.longitude = longitude


            # print(room)

            # await database_sync_to_async (self.save_message)()

            # Send message to room group
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'longitude': longitude,
                    'latitude':latitude,
                    'code': text_data_json['code'],
                }
            )



    # Receive message from room group
    async def chat_message(self, event):
        if event['code'] == "new_message":
            message = event['message']
            name=event['name']
            room_id=event['room']
            # Send message to WebSocket
            await self.send(text_data=json.dumps({
                'message': message,
                'name':name,
                'room': room_id,
                'code':event['code']
            }))
