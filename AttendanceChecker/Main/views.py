from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.files import File
from django.conf import settings
from .models import Message
# Create your views here.
def index(response):
    return render(response,"Main/home.html")
def roomFind(response):
    return render(response,"Main/findroom.html")
def room(request, room_name):
    username = request.GET.get("username", "Anonymous")
    messages = Message.objects.filter(room=room_name)[0:25]
    return render(request, 'Main/room.html',{'room_name':room_name, 'username':username, 'messages': messages})