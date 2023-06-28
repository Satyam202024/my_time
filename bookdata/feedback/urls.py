from django.urls import path
from .views import *
urlpatterns = [
    path('feedback/<int:pk>',FeedbackView.as_view()),
    path('feedback/rating/<str:book_id>/',BookFeedbackCountView.as_view()),

]
