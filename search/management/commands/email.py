"""
Custom django command, fetches customer favourites and send it by email
"""
from django.core.management.base import BaseCommand, CommandError
from django.core.mail import send_mail


class Command(
    BaseCommand
):  # Custom django command, fetches customer favourites and send it by email
    help = "Custom django command, fetches customer favourites and send it by email"

    def handle(self, *args, **options):
        send_mail('Bonjour de Pur Beurre',
            'Ceci est un message automatique, merci de na pas y répondre',
            'vincent.nowak@hotmail.fr',
            ['vincent.nowaczyk@protonmail.com'])
