"""URLS paths of home app"""
from django.urls import path
from . import views

def trigger_error(request):
    division_by_zero = 1/0


app_name = "home"
urlpatterns = [
    path("", views.index, name="index"),
    path("mentions-legales", views.mentions_legales, name="mentions"),
    path('sentry-debug', trigger_error),
]
