from django.urls import path,include
from .views import *
urlpatterns = [
    # path('bio/',AllBioViews.as_view(),name='BioView'),
    path('bio/<pk>',BioViews.as_view(),name='BioView'),
    path('bio/', BioSearchView.as_view(), name='bio-filter-by-name'),
]
