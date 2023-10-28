from django.urls import path
from .views import *
# from  .views import venue_csv,get_venue
from . import views
urlpatterns = [
    
    path('userview/<int:pk>/',UserView.as_view(),name='UserView'),
    path('usercreate/',UserCreate.as_view(),name='UserCreate'),
    path('bookview/<int:pk>/',BookView.as_view(),name='UserView'),
    path('recommendation/', RecommendationAPIView.as_view(), name='recommendation_api'),
    # path('books/filter/', BookFilterAPIView.as_view(), name='book-filter'),
    # path('csv/',views.venue_csv),
    # path('csvs/',views.get_venue)

]
