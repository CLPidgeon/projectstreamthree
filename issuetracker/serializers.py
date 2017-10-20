from rest_framework import serializers
from .models import Issue


class IssueSerializer(serializers.ModelSerializer):
    """Serializing the issues for the API"""
    class Meta:
        model = Issue
        fields = ('id', 'title', 'description', 'status', 'type', 'updated')
