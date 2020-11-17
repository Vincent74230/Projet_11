"""URLS paths of home app"""
from django.urls import path
from . import views

app_name = "home"
urlpatterns = [
    path("", views.index, name="index"),
    path("mentions-legales", views.mentions_legales, name="mentions"),
]
