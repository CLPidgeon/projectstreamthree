# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import sqlite3
import json
from django.http import HttpResponse


# Create your views here.
def bugs_data(request):

    conn = sqlite3.connect('db.sqlite3')

    c = conn.cursor()

    bug_status = c.execute("SELECT updated FROM bugs_bug WHERE status='Done';")

    bug_data = json.dumps(list(bug_status))

    return HttpResponse(bug_data, content_type='text/plain')


def features_data(request):

    conn = sqlite3.connect('db.sqlite3')

    c = conn.cursor()

    feature_status = c.execute("SELECT updated FROM features_feature WHERE status='Done';")

    feature_data = json.dumps(list(feature_status))

    return HttpResponse(feature_data, content_type='text/plain')


def charts(request):

    return render(request, 'charts.html')
