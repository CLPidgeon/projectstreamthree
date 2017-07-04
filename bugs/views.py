# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from bugs.serializers import BugSerializer
from bugs.models import Bug
from .forms import BugForm, CommentForm


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


@login_required(login_url='/login/')
def new_bug(request):

    if request.method == 'POST':
        form = BugForm(request.POST, request.FILES)
        if form.is_valid():

            bug = form.save(commit=False)
            bug.save()
            return redirect(bug_tracker)
    else:
        form = BugForm()

    return render(request, 'issuetracker/bugs/bugform.html', {'form': form})


def bug_tracker(request):

    bugs = Bug.objects.all()

    return render(request, 'issuetracker/bugs/bugs.html', {"bugs": bugs})


def bug_vote(request, id):

    bug = get_object_or_404(Bug, pk=id)

    return render(request, 'issuetracker/bugs/bug_vote.html', {'bug': bug})


def bug(request, bug_id):

    bug_ = get_object_or_404(Bug, pk=bug_id)
    args = {'bug': bug_}
    args.update(csrf(request))
    return render(request, 'issuetracker/bugs/bug.html', args)


@login_required(login_url='/login/')
def bug_comment(request, bug_id):

    bug = get_object_or_404(Bug, pk=bug_id)

    if request.method == 'POST':

        form = CommentForm(request.POST)

        if form.is_valid():
            comments = form.save(commit=False)
            comments.bug = bug
            comments.save()
            return redirect(reverse('bug', args={bug.pk}))
    else:

        form = CommentForm()

    args = {
        'form': form,
        'form_action': reverse('bug_comment', args={bug.id}),
        'button_text': 'Add Comment'
    }

    args.update(csrf(request))

    return render(request, 'issuetracker/bugs/commentform.html', args)
