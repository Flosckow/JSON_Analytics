from django.contrib import admin
from django.urls import path

from .views import GetJson, render_html

urlpatterns = [
    path('file/', GetJson.as_view()),
    path('render/', render_html, name='render'),
]