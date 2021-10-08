from django.shortcuts import render, redirect
from django.core.files import File
from django.conf import settings
from .models import Message, room
from Account.models import CustomUser
import time
# Create your views here.
def index(request):
    if request.user.is_authenticated:
        User = CustomUser.objects.filter(username = request.user.username)[0]
        User.lastActivity = int(time.time())
        User.save()
        return render(request,"Main/home.html")
    else:
        return render(request,"Main/home.html")
def roomFind(request):
    if request.user.is_authenticated: 
        User = CustomUser.objects.filter(username = request.user.username)[0]
        User.lastActivity = int(time.time())
        User.save()
        return render(request,"Main/findroom.html")
    else:
        return render(request,"Main/findroom.html")
def roomFound(request, room_name):
    User = CustomUser.objects.filter(username = request.user.username)[0]
    User.lastActivity = int(time.time())
    User.save()
    username = request.GET.get("username", "Anonymous")
    if room.objects.filter(roomname= room_name).exists():
        if request.user.username in room.objects.get(roomname = room_name).subscribers:
            roomTemp = room.objects.filter(roomname = room_name)  
            usersTemp = roomTemp[0].subscribers
            messages = Message.objects.filter(room=room.objects.get(roomname = room_name))[0:25]
            return render(request, 'Main/room.html',{'room_name':room_name, 'username':username, 'messages': messages,'users':usersTemp})
        else:
            rm = room.objects.get(roomname = room_name)
            rm.subscribers.append(request.user.username)
            rm.save()
            messages = Message.objects.filter(room=room.objects.get(roomname = room_name))[0:25]
            return render(request, 'Main/room.html',{'room_name':room_name, 'username':"username", 'messages': messages,'type':"typeUsers"})
    else:
        room.objects.get_or_create(roomname = room_name, subscribers = [request.user.username])
        return render(request, 'Main/room.html',{'room_name':room_name, 'username':username})
