from django.http import HttpResponseRedirect
from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
import json
import os
from django.conf import settings
import plotly.graph_objects as go
from .models import User
from .serializers import UserSerialazers


class GetAllUsers(ListAPIView):
    queryset = User.objects.filter(is_active=True).order_by('-date_joined')
    serializer_class = UserSerialazers


class UserView(RetrieveAPIView):
    model = User
    serializer_class = UserSerialazers

    def retrieve(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            print('You auth')
        print('You should not pass!!')





