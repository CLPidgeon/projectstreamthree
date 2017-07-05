# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404, reverse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth.decorators import login_required
from features.serializers import FeatureSerializer
from features.models import Feature, Comments
from forms import FeatureForm, CommentForm
from django.template.context_processors import csrf


# Create your views here.
class FeatureView(APIView):

    def get(self, request, pk=None):

        if pk is None:

            feature_items = Feature.objects.all()
            serializer = FeatureSerializer(feature_items, many=True)
            serialized_data = serializer.data

            return Response(serialized_data)

        else:

            feature = Feature.objects.get(id=pk)
            serializer = FeatureSerializer(feature)
            serialized_data = serializer.data

            return Response(serialized_data)

    def post(self, request):

        serializer = FeatureSerializer(data=request.data)
        if not serializer.is_valid():

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        else:

            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request, pk):

        feature = Feature.objects.get(id=pk)
        serializer = FeatureSerializer(feature, data=request.data)

        if not serializer.is_valid():

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        else:

            serializer.save()

            return Response(serializer.data)

    def delete(self, request, pk):

        feature = Feature.objects.get(id=pk)
        feature.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


@login_required(login_url='/login/')
def feature_tracker(request):

    features = Feature.objects.all()

    return render(request, 'issuetracker/features/features.html', {"features": features})


@login_required(login_url='/login/')
def new_feature(request):

    if request.method == 'POST':
        form = FeatureForm(request.POST, request.FILES)
        if form.is_valid():

            feature = form.save(commit=False)
            feature.save()
            return redirect(feature_tracker)
    else:
        form = FeatureForm()

    return render(request, 'issuetracker/features/featureform.html', {'form': form})


def feature(request, feature_id):

    feature_ = get_object_or_404(Feature, pk=feature_id)
    args = {'feature': feature_}
    args.update(csrf(request))
    return render(request, 'issuetracker/features/feature.html', args)


@login_required(login_url='/login/')
def feature_comment(request, feature_id):

    feature = get_object_or_404(Feature, pk=feature_id)

    if request.method == 'POST':

        form = CommentForm(request.POST)

        if form.is_valid():
            comments = form.save(commit=False)
            comments.feature = feature
            comments.save()
            return redirect(reverse('feature', args={feature.pk}))
    else:

        form = CommentForm()

    args = {
        'form': form,
        'form_action': reverse('feature_comment', args={feature.id}),
        'button_text': 'Add Comment'
    }

    args.update(csrf(request))

    return render(request, 'issuetracker/features/commentform.html', args)


def feature_vote(request, feature_id):

    feature = get_object_or_404(Feature, pk=feature_id)

    return render(request, 'issuetracker/features/feature_vote.html', {'feature': feature})