# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from bugs.serializers import BugSerializer
from bugs.models import Bug
from forms import BugForm


# Create your views here.
class BugView(APIView):

    def get(self, request, pk=None):

        if pk is None:

            bug_items = Bug.objects.all()
            serializer = BugSerializer(bug_items, many=True)
            serialized_data = serializer.data

            return Response(serialized_data)

        else:

            bug = Bug.objects.get(id=pk)
            serializer = BugSerializer(bug)
            serialized_data = serializer.data

            return Response(serialized_data)

    def post(self, request):

        serializer = BugSerializer(data=request.data)
        if not serializer.is_valid():

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        else:

            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request, pk):

        bug = Bug.objects.get(id=pk)
        serializer = BugSerializer(bug, data=request.data)

        if not serializer.is_valid():

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        else:

            serializer.save()

            return Response(serializer.data)

    def delete(self, request, pk):

        bug = Bug.objects.get(id=pk)
        bug.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


def new_bug(request):

    if request.method == 'POST':
        form = BugForm(request.POST, request.FILES)
        if form.is_valid():

            bug = form.save(commit=False)
            bug.save()
            return redirect(bug_tracker)
    else:
        form = BugForm()

    return render(request, 'issuetracker/bugform.html', {'form': form})


def bug_tracker(request):

    bugs = Bug.objects.all()

    return render(request, 'issuetracker/bugs.html', {"bugs": bugs})
