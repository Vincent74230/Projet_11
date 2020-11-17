"""
Custom django-admin command, fetches and login datas from OFF server
"""
from django.core.management.base import BaseCommand, CommandError
from search.models import Products
import requests
from requests.exceptions import HTTPError, ConnectionError
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

CATEGORIES = ["fr:Pâtes à tartiner", "Ice creams and sorbets", "Sodas", "Crisps"]
NUTRISCORES = ["a", "b", "c", "d", "e"]


class Command(
    BaseCommand
):  # Custom django-admin command, fetches and login datas from OFF server
    help = "Fetches datas from openfoodfacts database and logs into server database"

    def handle(self, *args, **options):
        CLEAR_PRODUCTS = Products.objects.all()

        CLEAR_PRODUCTS.delete()

        for category in CATEGORIES:
            for nutriscore in NUTRISCORES:
                try:
                    payload = {
                        "action": "process",
                        "json": 1,
                        "tagtype_0": "categories",
                        "tag_contains_0": "contains",
                        "tag_0": category,
                        "tagtype_1": "nutrition_grades",
                        "tag_contains_1": "contains",
                        "tag_1": nutriscore,
                        "countries": "France",
                        "page_size": 500,
                        "sort_by": "unique_scans_n",
                    }
                    response = requests.get(
                        "https://world.openfoodfacts.org/cgi/search.pl",
                        params=payload,
                        headers={"User-Agent": "Apptest - GNU/Linux - Version 0.1"},
                    )
                    response = response.json()
                    response = response["products"]
                except HTTPError as err:
                    print(
                        "Openfoodfacts server might be busy or has crashed, or check your connection : {}\n".format(
                            err
                        )
                    )

                except ConnectionError as con_err:
                    print(
                        "Openfoodfacts server in not reachable, check your connexion {}".format(
                            con_err
                        )
                    )

                for item in response:
                    try:
                        # We want to check if the provided url is correct
                        url_validator = URLValidator()
                        url_validator(item["image_small_url"])
                        # Let's try to log this on DB
                        query = Products(
                            barcode=item["id"],
                            image=item["image_small_url"],
                            category=item["categories"],
                            name=item["product_name"],
                            nutriscore=item["nutrition_grades"],
                        )
                        query.save()
                    except KeyError:#If an attribute is missing, pass
                        pass
                    except ValidationError:
                        query = Products(
                            barcode=item["id"],
                            image=None,
                            category=item["categories"],
                            name=item["product_name"],
                            nutriscore=item["nutrition_grades"],
                        )
                        query.save()

            print("Extraction of {} category, done.".format(category))
        print("Extraction DONE. Dabatbase up-to-date")
