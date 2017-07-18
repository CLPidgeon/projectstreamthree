# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import json
from django.http import HttpResponse
from features.models import Feature
import datetime


# Create your views here.
def featuredata(request):

    feature_status = Feature.objects.all()

    features_data = []

    def datetime_handler(x):
        if isinstance(x, datetime.datetime):
            return x.isoformat()

    for feature in feature_status:
        feature_data = {
            'title': feature.title,
            'description': feature.description,
            'status': feature.status,
            'updated': feature.updated}
        features_data.append(feature_data)
    feature_dataset = json.dumps(features_data, default=datetime_handler)

    return HttpResponse(feature_dataset, content_type='text/plain')


def features_charts(request):

    return render(request, 'charts.html')
