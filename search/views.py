"""Biggest app of project: contains search algorithm"""
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import Products
from django.contrib.auth.models import User
import openfoodfacts


def index(request):
    """Algorithm that fetches substitutes"""
    context = {}
    if request.method == "POST":
        user_question = request.POST.get("UserQuestion")
        nutriscores = ["a", "b", "c", "d", "e"]
        substitutes_list = []
        try:
            result = Products.objects.filter(name__icontains=user_question)
            result = result[0]
            categories = result.category
            cat = categories.split(",")
            cat = cat[-1]#We pick substitutes on the last tag of 'categories'
            substitutes = Products.objects.filter(category__icontains=cat)
            for nutriscore in nutriscores:#We make a list with best substitues ahead
                sub = substitutes.filter(nutriscore=nutriscore)
                for element in sub:
                    substitutes_list.append(element)

            context = {
                "UserQuestion": result.name,
                "Image": result.image,
                "substitutes": substitutes_list,
            }
        except IndexError:
            context = {"UserQuestion": "Pas de résultats... Tapez une autre demande"}

    return render(request, "search/index.html", context)


def detail(request, UserChoice):
    """Displays a products specifications"""
    product = get_object_or_404(Products, barcode=UserChoice)
    try:
        infos = openfoodfacts.products.get_product(UserChoice)
        infos = infos["product"]
        context = {"product": product, "infos": infos}
    except:
        raise Http404("La page demandée n'existe pas")

    return render(request, "search/detail.html", context)


@login_required
def register_substitute(request, UserChoice):
    """Log favourite on user account, uses many-to-many field in Products model"""
    try:
        favourite_product = Products.objects.filter(barcode=UserChoice)
        favourite_product = favourite_product[0]
        favourite_product.favourites.add(request.user.id)
        return render(request, "search/register_fav_ok.html", {})
    except:
        raise Http404("Le produit demandé n'existe pas")


@login_required
def favourites(request):
    """fetches user's favourites, returns a list"""
    fav = Products.objects.filter(favourites=request.user.id)
    user_favourites = []
    for element in fav:
        user_favourites.append(element)
    context = {"user_favourites": user_favourites}
    return render(request, "search/my_food.html", context)
