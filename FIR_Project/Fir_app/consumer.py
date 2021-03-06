import json
from asgiref.sync import async_to_sync, sync_to_async
from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
from .models import Alerts,UserData,Police_Station_data
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

    def save_alert(self):
        udta = UserData.objects.get(user__username=self.username)
        station = Police_Station_data.objects.get(sho__username=self.sho)
        alerts = Alerts(user=udta, main_area=self.subdistrict + " " + self.district, station=station)
        alerts.save()


    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        if text_data_json['code'] == 'new_message':
            district = text_data_json['district']
            subdistrict = text_data_json['subdistrict']
            username = text_data_json['username']
            sho = text_data_json['sho_uname']

            print(username)
            self.username=username
            self.sho=sho
            self.district = district
            self.subdistrict = subdistrict

            # print(room)

            await database_sync_to_async (self.save_alert)()

            # Send message to room group
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'district': district,
                    'subdistrict':subdistrict,
                    'code': text_data_json['code'],
                    'sho':sho,
                    'name':text_data_json['name'],
                }
            )



    # Receive message from room group
    async def chat_message(self, event):
        if event['code'] == "new_message":

            await self.send(text_data=json.dumps({
                'message':'Message Sent',
                'sho':event['sho'],
                'district':event['district'],
                'subdistrict':event['subdistrict'],
                'name':event['name'],
            }))
