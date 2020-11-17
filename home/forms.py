"""UserQuestion form"""
from django import forms


class UserQuestion(forms.Form):
    """Contains user question field"""
    question = forms.CharField(max_length=100)
