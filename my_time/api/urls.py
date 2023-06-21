from django.urls import path
from .views import *
urlpatterns = [
    path('upload/',UploadView.as_view(),name='upload'),
]
