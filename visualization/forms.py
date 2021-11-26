from django import forms
from django.forms import (
    BooleanField,
    CharField,
    ChoiceField,
    DateField,
    DateTimeField,
    DecimalField,
    FileField,
    Form,
    IntegerField,
    ModelChoiceField,
    ModelForm,
    formset_factory,
)


class DataForm(Form):
    file = FileField()
