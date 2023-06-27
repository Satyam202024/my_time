from django.urls import path
from .views import *
urlpatterns = [
    
    path('userview/<int:pk>',UserView.as_view(),name='UserView'),
    path('usercreate/',UserCreate.as_view(),name='UserCreate'),
    path('bookview/<int:pk>',BookView.as_view(),name='UserView'),
]
