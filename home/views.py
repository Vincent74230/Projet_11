'''Views module of home app'''
from django.shortcuts import render
from .forms import UserQuestion


def index(request):
    """Returns app main page"""
    form = UserQuestion()
    return render(request, "home/index.html", {"form": form})


def mentions_legales(request):
    """Returns credits page"""
    return render(request, "home/mentions_legales.html", {})
