from django.urls import path
from .views import UserView,UserViewList

urlpatterns = [
    path('user/<int:pk>/', UserView.as_view(), name='update-user'),
    path('user/',UserViewList.as_view(), name='update-user'),
]
