from __future__ import unicode_literals
from django.shortcuts import render


def eihl(request):
    return render(request, 'leaguepages/eihl.html')


def GB(request):
    return render(request, 'leaguepages/GB.html')
