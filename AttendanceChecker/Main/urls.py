from django.urls import path
from . import views
urlpatterns=[
    path('',views.index),
    path('roomfind/',views.roomFind),
    path("roomfind/<str:room_name>/", views.roomFound, name="room"),
    path('<str:Code>/classMain/discussion/',views.discussionRoom),
    path('<str:Code>/classMain/room/',views.roomClass),
    path('<str:Code>/classMain/',views.classMain),
    path('<str:Code>/classTemp/',views.classTemp),
    path('createClass/',views.createClass),
    path('joinClass/',views.joinClass),
]