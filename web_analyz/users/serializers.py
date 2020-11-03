from rest_framework import serializers

from .models import User


class UserSerialazers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'company', 'email']