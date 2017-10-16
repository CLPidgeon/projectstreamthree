from __future__ import unicode_literals
from django.shortcuts import render


def fantasy_eihl(request):
    return render(request, 'leaguepages/eihl.html')
