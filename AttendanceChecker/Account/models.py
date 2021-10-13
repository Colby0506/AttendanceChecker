from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.contrib.postgres.fields import ArrayField
import random, string
# Create your models here.
class CustomUser(AbstractUser):    
    id = models.AutoField(primary_key=True)
    date_joined = models.DateTimeField(verbose_name="date_joined", auto_now=True,null=True)
    last_login = models.DateTimeField(verbose_name="last_login", auto_now_add=True,null=True)
    is_teacher = models.BooleanField(verbose_name="is_teacher",null=True)
    is_student = models.BooleanField(verbose_name="is_student",null=True)
    lastActivity = models.IntegerField(null = True)
    friends = ArrayField(models.CharField(max_length = 255),null=True)
    username = models.CharField(max_length=255,unique=True)
    friendCode= models.CharField(max_length=255,unique =True,null=True)
    def __str__(self):
        return self.username
#class UserPreferences(models.Model):
#    user = models.OneToOneField(to=User,on_delete=models.CASCADE)
    
