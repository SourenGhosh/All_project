from django.forms import ModelForm
from .models import book_shelf

class book_form(ModelForm):
    class Meta:
        model = book_shelf
        exclude = ()  # this says to include all fields from model to the form
