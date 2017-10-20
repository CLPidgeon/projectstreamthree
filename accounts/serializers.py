from rest_framework import serializers
from .models import User


# Code taken from Code Insitute Lesson
class UserSerializer(serializers.ModelSerializer):
    """Serializing Users username and password for API use"""
    class Meta:
        model = User
        fields = ('username', 'password')
