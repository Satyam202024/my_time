from django.contrib import admin
from django.urls import path,include
from .views import UserView,CreateView,UserLoginView

urlpatterns = [
     path('UserData/<pk>', UserView.as_view()),
     path('UserCreate/', CreateView.as_view()),
     path('UserLogin/', UserLoginView.as_view())
]
