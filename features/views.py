# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth.decorators import login_required
from features.serializers import FeatureSerializer
from features.models import Feature
from forms import FeatureForm, CommentForm


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


def feature_comment(request, id):

    feature = get_object_or_404(Feature, pk=id)

    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():

            comments = form.save(commit=False)
            comments.save()
            return redirect(feature_tracker)
    else:
        form = CommentForm

    return render(request, 'issuetracker/features/feature.html', {'feature': feature, 'form': form})
