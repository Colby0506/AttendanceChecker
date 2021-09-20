from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    date_joined = models.DateTimeField(verbose_name="date_joined", auto_now=True,null=True)
    last_login = models.DateTimeField(verbose_name="last_login", auto_now_add=True,null=True)
    is_teacher = models.BooleanField(verbose_name="is_teacher",null=True)
    is_student = models.BooleanField(verbose_name="is_student",null=True)
    def __str__(self):
        return self.username