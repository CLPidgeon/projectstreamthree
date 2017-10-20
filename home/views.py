from __future__ import unicode_literals
from django.shortcuts import render


def get_index(request):
    """Gets home page"""
    return render(request, 'index.html')


def get_fantasy(request):
    """Gets fantasy ice hockey page"""
    return render(request, 'fantasyIH.html')


def get_about(request):
    """Gets about page"""
    return render(request, 'about.html')


def get_contact(request):
    """Gets contact page"""
    return render(request, 'contact.html')
