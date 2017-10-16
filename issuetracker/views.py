from __future__ import unicode_literals
from django.shortcuts import render, redirect, reverse, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from .serializers import IssueSerializer
from .models import Issue
from .forms import IssueForm, CommentForm


class IssueView(APIView):

    def get(self, request, pk=None):
        if pk is None:
            issue_items = Issue.objects.all()
            serializer = IssueSerializer(issue_items, many=True)
            serialized_data = serializer.data
            return Response(serialized_data)
        else:
            issue = Issue.objects.get(id=pk)
            serializer = IssueSerializer(issue)
            serialized_data = serializer.data
            return Response(serialized_data)

    def post(self, request):
        serializer = IssueSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request, pk):
        issue = Issue.objects.get(id=pk)
        serializer = IssueSerializer(issue, data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer.save()
            return Response(serializer.data)

    def delete(self, request, pk):
        issue = Issue.objects.get(id=pk)
        issue.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@login_required(login_url='/login/')
def new_issue(request):
    if request.method == 'POST':
        form = IssueForm(request.POST, request.FILES)
        if form.is_valid():
            issue_new = form.save(commit=False)
            issue_new.save()
            return redirect(issue_tracker)
    else:
        form = IssueForm()
    return render(request, 'issuetracker/issueform.html', {'form': form})


@login_required(login_url='/login/')
def issue_tracker(request):
    issues = Issue.objects.all()
    return render(request, 'issuetracker/all_issues.html', {"issues": issues})


def issue_detail(request, issue_id):
    issue_ = get_object_or_404(Issue, pk=issue_id)
    args = {'issue': issue_}
    args.update(csrf(request))
    return render(request, 'issuetracker/issue.html', args)


@login_required(login_url='/login/')
def issue_comment(request, issue_id):
    issue = get_object_or_404(Issue, pk=issue_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comments = form.save(commit=False)
            comments.issue = issue
            comments.save()
            return redirect(reverse('issue', args={issue.pk}))
    else:
        form = CommentForm()
    args = {
        'form': form,
        'form_action': reverse('issue_comment', args={issue.id}),
        'button_text': 'Add Comment'
    }
    args.update(csrf(request))
    return render(request, 'issuetracker/commentform.html', args)


@login_required(login_url='/login/')
def issue_vote(request, issue_id):
    issue = Issue.objects.get(id=issue_id)
    issue.issue_votes.create(issue=issue_id, user=request.user)
    return render(request, 'issuetracker/issue_vote.html', {'issue': issue})
