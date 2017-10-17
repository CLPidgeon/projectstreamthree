from rest_framework import serializers
from .models import Issue


class IssueSerializer(serializers.ModelSerializer):
    "Serializing the issues"
    class Meta:
        model = Issue
        fields = ('id', 'title', 'description', 'status', 'type', 'updated')
