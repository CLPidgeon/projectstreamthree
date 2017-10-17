from __future__ import unicode_literals
from django.shortcuts import render


def fantasy_eihl(request):
    "Retrieves the fantasy ice hockey league table"
    return render(request, 'leaguepages/eihl.html')
