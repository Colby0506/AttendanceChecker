from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.files import File
from django.conf import settings

# Create your views here.
def index(response):
    return render(response,"Main/home.html")
def roomFind(response):
    return render(response,"Main/findroom.html")
def room(request, room):
    username = request.GET.get('username')
    return render(request, 'Main/room.html',{'roomName':roomName, 'username':username})