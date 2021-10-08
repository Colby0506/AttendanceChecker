from django.urls import path
from . import views
urlpatterns=[
    path('',views.index),
    path('roomfind/',views.roomFind),
    path("roomfind/<str:room_name>/", views.roomFound, name="room"),
]