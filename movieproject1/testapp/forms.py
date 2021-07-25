from django import forms
from django.forms import fields
from testapp.models import Movie

class MovieForm(forms.ModelForm):
    class Meta:
        model=Movie
        fields='__all__'