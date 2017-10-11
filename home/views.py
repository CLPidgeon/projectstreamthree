from __future__ import unicode_literals
from django.shortcuts import render


def get_index(request):
    return render(request, 'index.html')


def fantasy(request):
    return render(request, 'fantasyIH.html')
