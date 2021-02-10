"""
Custom django command, fetches customer favourites and send it by email
"""
from django.core.management.base import BaseCommand, CommandError
from django.core.mail import send_mail
from django.template.loader import render_to_string
#from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.models import User
from ...models import Products


class Command(
    BaseCommand
):  # Custom django command, fetches customer favourites and send it by email
    help = "Custom django command, fetches customer favourites and send it by email"
    def handle(self, *args, **options):
        all_users=User.objects.all()
        for user in all_users:
            if user.email:
                
                fav = Products.objects.filter(favourites=user.id)
                user_favourites = []
                for element in fav:
                    user_favourites.append(element)
                
                msg_html = render_to_string('email.html',{})
                send_mail(
                    "Bonjour {}, c'est Pur Beurre!".format(user.username),
                    'Ceci est un message très important',
                    'vincent.nowak@hotmail.fr',
                    [user.email],
                    html_message=msg_html,)





                """
                favourites=Products.objects.filter(favourites=user.id)
                if favourites:
                    send_mail('Bonjour de Pur Beurre',
                        'Bonjour {},\nVoici vos produits favoris : {}\nRevenez nous voir très vite'.format(user.username,favourites),
                        'vincent.nowak@hotmail.fr',
                        [user.email])
                else:
                    send_mail('Bonjour de Pur Beurre',
                        "Vous n'avez pas enregistré de produits favoris chez nous, c'est dommage c'est les soldes chez nous!!!",
                        "vincent.nowak@hotmail.fr",
                        [user.email])
"""