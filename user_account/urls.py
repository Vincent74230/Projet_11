"""Contains urls paths of ser_account app"""
from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="user_account"),
    path("sign_in", views.register_page, name="sign_in"),
    path("login", views.login_page, name="login"),
    path("logout", views.logoutUser, name="logout"),
]
