# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import sqlite3
import pandas as pd
import json


# Create your views here.
def bug_data(request):

    fields = {
        '_id': False, 'title': True, 'description': True,
        'status': True, 'updated': True,
    }

    with sqlite3.connect('db.sqlite3') as conn:

        bug_table = conn('bugs_bug')

        bugs_data = bug_table.find(fields)

        return json.dumps(list(bugs_data))


def feature_data(request):

    conn = sqlite3.connect('db.sqlite3')

    feature_status = pd.read_sql_query('SELECT * FROM features_feature', conn)

    return json.dumps(feature_status)


def charts(request):

    return render(request, 'charts.html')
