from django.db import models
from django.conf import settings
from django.contrib.postgres.fields import ArrayField
from django.db.models.deletion import CASCADE
# Create your models here.
class room(models.Model):
    subscribers = ArrayField(models.CharField(max_length = 255))
    roomname = models.TextField(max_length = 255,unique = True)
    def __str__(self):
        return self.subscribers

class Message(models.Model):
    username = models.CharField(max_length=255)
    room = models.ForeignKey(room, on_delete=models.CASCADE)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ('date_added',)

class Classroom(models.Model):
    className = models.CharField(max_length=255,unique = True)
    accessCode = models.TextField(max_length=255, unique = True)
    students = ArrayField(models.CharField(max_length=255))

class DiscussionRoom(models.Model):
    Class = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    subscribers = ArrayField(models.CharField(max_length = 255))
    roomname = models.TextField(max_length = 255,unique = True)
    accessCode = models.TextField(max_length=255, unique = True)

class DiscussionPost(models.Model):
    discussionRoom = models.ForeignKey(DiscussionRoom,on_delete=models.CASCADE)
    postType= models.CharField(max_length=100)
    postSubject = models.CharField(max_length=255)
    postContent = models.TextField()
    username = models.CharField(max_length=255)
    date_added = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ('date_added',)

class DiscussionResponse(models.Model):
    post = models.ForeignKey(DiscussionPost,on_delete=CASCADE)
    username = models.CharField(max_length=255)
    replyContent= models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ('date_added',)

class Assigments(models.Model):
    name = models.CharField(max_length=255)
    fileSubmission = models.FileField()
    dueDate = models.DateTimeField()
    tests = ArrayField(models.TextField(),null=True)


class roomClass(models.Model):
    Class = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    subscribers = ArrayField(models.CharField(max_length = 255))
    roomname = models.TextField(max_length = 255,unique = True)

class MessageRoom(models.Model):
    username = models.CharField(max_length=255)
    room = models.ForeignKey(roomClass, on_delete=models.CASCADE)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ('date_added',)