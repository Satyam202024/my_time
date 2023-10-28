from django.urls import path
from .views import MemberView,MemberViewList,TeamView,TeamViewList, GetAllTeamMembers,NextBillPayerView

urlpatterns = [
    path('member/<int:pk>/', MemberView.as_view(), name='update-user'),
    path('members/',MemberViewList.as_view(), name='update-user'),
    path('team/<int:pk>/', TeamView.as_view(), name='update-user'),
    path('teams/',TeamViewList.as_view(), name='update-user'),
    path('all-team/', GetAllTeamMembers.as_view()),
     path('next-bill-payer/', NextBillPayerView.as_view()),
]

