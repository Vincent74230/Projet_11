"""Url paths of search app"""
from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="search_index"),
    path("detail/<str:UserChoice>/", views.detail, name="search_detail"),
    path(
        "register_sub/<str:UserChoice>",
        views.register_substitute,
        name="search_register_substitute",
    ),
    path("favourites", views.favourites, name="search_favourites"),
]
