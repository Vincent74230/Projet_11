"""Contains functions of user_account app"""
from django.shortcuts import render, redirect
from .forms import RegisterForm
from search.models import NewsLetter
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def index(request):
    """If user is logged in, shows user_account index page"""
    if request.user.is_authenticated:
        if request.method == "POST":
            context = {}
            if request.POST.get("newsletter") == "unsubscribe":
                newsletter = NewsLetter(request.user.id, newsletter_registration=False)
                newsletter.save()
                return render(request, "user_account/index.html", context)
            elif request.POST.get("newsletter") == "subscribe":
                newsletter = NewsLetter(request.user.id, newsletter_registration=True)
                newsletter.save()
                return render(request, "user_account/index.html", context)
        context = {}
        return render(request, "user_account/index.html", context)
    else:
        return redirect("/")


def register_page(request):
    """Checks user creation form conformity"""
    Registration = RegisterForm()
    if request.method == "POST":
        Registration = RegisterForm(request.POST)
        newsletter_choice = request.POST.get("newsletter")
        if Registration.is_valid():
            Registration.save()
            if newsletter_choice:
                user = Registration.cleaned_data.get("username")
                user_id = User.objects.filter(username=user)
                user_id = user_id[0].id
                newsletter = NewsLetter(user_id, newsletter_registration=True)
                newsletter.save()
            else:
                user = Registration.cleaned_data.get("username")
                user_id = User.objects.filter(username=user)
                user_id = user_id[0].id
                newsletter = NewsLetter(user_id, newsletter_registration=False)
                newsletter.save()
            user = Registration.cleaned_data.get("username")
            messages.success(request, "Votre compte a bien été créé" + user)
            return redirect("login")

    context = {"RegisterForm": Registration}
    return render(request, "user_account/register_page.html", context)


def login_page(request):
    """Login page, checks username and password"""
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(
            request, username=username, password=password
        )  # check if user is in DB
        if user is not None:
            login(request, user)
            return redirect("/")  # redirect to homepage
        else:
            messages.info(
                request, "Votre nom d'utilisateur ou mot de passe est incorrect"
            )

    context = {}
    return render(request, "user_account/login.html", context)


@login_required
def logoutUser(request):
    """Logout function, login required"""
    logout(request)
    return redirect("login")
