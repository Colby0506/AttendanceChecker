from django.urls import path
from .views import SignUpView, AccountPageView
urlpatterns = [
    path('signup/',SignUpView),
    path('page/',AccountPageView)
]