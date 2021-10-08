import json
from os import listxattr

from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from .models import Message, room
from asyncio import sleep
from Account.models import CustomUser
import time

class ChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept() 
        #while True:
        #    await self.checkUsers()
        #     await sleep(20)

    
    async def disconnect(self, close_code):
        # Leave room
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
    
    # Receive message from web socket
    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        username = data['username']
        room = data['room']

        await self.save_message(username, room, message)

        # Send message to room group
        #await self.channel_layer.group_send(
        #    self.room_group_name,
        #    {
        #        'type': 'chat_message',
        #        'message': message,
        #        'username': username,
        #        'roomname': room
        #    }
        #)
        data2 = []
        data2.append(['messageUser', message])
        data2.append(['usernameUser', username])
        list2 = await self.checkUsers(room)
        listFinal = data2 + list2
        await self.send(text_data=json.dumps({
            'data':dict(listFinal)
        }))
    
    # Receive message from room group
#    async def chat_message(self, event):
#        message = event['message']
#        username = event['username']
#        roomname = event['roomname']
#        # Send message to WebSocket
#        data = []
#        data.append(['messageUser', message])
#        data.append(['usernameUser', username])
#        await self.send(text_data=json.dumps({
#            'data':dict(data)
#        }))

    @sync_to_async
    def save_message(self, username, roomdef, message):
        m = Message()
        m.room = room.objects.get(roomname = roomdef)
        m.content = message
        m.username = username
        m.save()
    
    @sync_to_async
    def createRoom(self, roomdef):
        room.objects.update_or_create(roomname = roomdef)

    @sync_to_async
    def addUserToRoom(self, username, roomdef):
        roomTemp = room.objects.get(roomname = roomdef)
        roomTemp.subscribers.add(username)

    @staticmethod
    @sync_to_async
    def checkUsers(roomname):
        roomTemp = room.objects.filter(roomname = roomname)  
        users = roomTemp[0].subscribers
        currentTime = int(time.time())
        dictionary = {}
        for i in users:
            customUser = CustomUser.objects.filter(username = i)[0]
            if (currentTime - customUser.lastActivity) > 900:
                #NA means Not Active
                dictionary[i] = "NA"
            else:
                dictionary[i] = "Active"
        listTemp = []
        for k,v in dictionary.items():
            listTemp.append((k,v))
        return listTemp
