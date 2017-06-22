# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from features.serializers import FeatureSerializer
from features.models import Feature
from forms import FeatureForm


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


def feature_tracker(request):

    features = Feature.objects.all()

    return render(request, 'issuetracker/features.html', {"features": features})


def new_feature(request):

    if request.method == 'POST':
        form = FeatureForm(request.POST, request.FILES)
        if form.is_valid():

            feature = form.save(commit=False)
            feature.save()
            return redirect(feature_tracker)
    else:
        form = FeatureForm()

    return render(request, 'issuetracker/featureform.html', {'form': form})
