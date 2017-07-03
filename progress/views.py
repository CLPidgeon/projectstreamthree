# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import sqlite3
import pandas as pd


# Create your views here.
def charts(request):
    conn = sqlite3.connect('db.sqlite3')
    bug_status = pd.read_sql_query('SELECT status, updated FROM bugs_bug WHERE status="Done";', conn)

    feature_status = pd.read_sql_query('SELECT status, updated FROM features_feature WHERE status="Done"', conn)

    conn.close()

    return render(request, 'charts.html', {'bug_status': bug_status, 'feature_status': feature_status})


