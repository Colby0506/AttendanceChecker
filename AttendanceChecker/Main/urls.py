from django.urls import path
from . import views
urlpatterns=[
    path('',views.index),
    path('roomfind/',views.roomFind),
    path('room/<str:room_name>/', views.room, name='room'),
]