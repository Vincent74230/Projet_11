"""Contains one model of search app : Products"""
from django.db import models
from django.contrib.auth.models import User


class Products(models.Model):
    """This table contains 5 attributes and MTM fields"""
    barcode = models.BigIntegerField(primary_key=True)
    image = models.URLField(null=True, default=None, blank=True)
    name = models.CharField(max_length=120)
    category = models.TextField(null=True, default=None, blank=True)
    nutriscore = models.CharField(max_length=5)
    favourites = models.ManyToManyField(User)

    def __str__(self):
        return self.name

class NewsLetter(models.Model):
    """One-to-one field to User, contains newletter boolean"""
    newsletter = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
        )
    newsletter_registration = models.BooleanField(default=False)

    def __str__(self):
        return "%s registration to newsletter is %s" % (self.newsletter.username, self.newsletter_registration)
