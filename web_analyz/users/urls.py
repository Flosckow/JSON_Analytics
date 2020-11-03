from django.contrib import admin
from django.urls import path

from .views import GetAllUsers, UserView

urlpatterns = [
    path('all/', GetAllUsers.as_view(), name='get_all_users'),
    path('one-users/<int:pk>/', UserView.as_view(), name='get_one_user')
]