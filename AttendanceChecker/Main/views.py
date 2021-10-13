from django.shortcuts import render, redirect
from django.core.files import File
from django.conf import settings
from .models import Message, room, DiscussionRoom, DiscussionPost, Classroom
from Account.models import CustomUser
import string, random,time
# Create your views here.

def discussionRoom(request,Code):
    if DiscussionRoom.objects.filter(accessCode = Code).exists():
        return render(request, 'Main/discussionRoom.html',{'name':Code})
    else:
        return redirect("http://127.0.0.1:8000")
def classMain(request,Code):
    if Classroom.objects.filter(accessCode = Code).exists():
        return render(request, 'Main/classMainPage.html',{'name':Code})
    else:
        return redirect("http://127.0.0.1:8000")
def classTemp(request,Code):
    if CustomUser.objects.filter(username = request.user.username)[0].is_teacher:
        Classroom.objects.get_or_create(className=Code,accessCode = randomCodeGen(), students = [request.user.username])
        ClassroomTemp = Classroom.objects.filter(className = Code)[0]
        DiscussionRoom.objects.get_or_create(Class=Code,accessCode = ClassroomTemp.accessCode, subscribers = [request.user.username])
        return redirect("http://127.0.0.1:8000/"+ ClassroomTemp.accessCode+"/classMain/")
    else:
        return redirect("http://127.0.0.1:8000")
def createClass(request):
    return render(request,"Main/createClass.html")
def joinClass(request):
    return render(request,"Main/joinClass.html")
def roomClass(request, Code):
    return render(request,'Main/roomClass.html')
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
def randomCodeGen():
    while True:
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for i in range(8))
        if Classroom.objects.filter(accessCode = password).exists():
            continue
        else:
            break
    return password