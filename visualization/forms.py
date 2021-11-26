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
import os
from django.core.exceptions import ValidationError


class DataForm(Form):
    file = FileField()

    def clean_file(self):
        data = self.cleaned_data['file']
        extension = os.path.splitext(data.name)[1]
        valid_extensions = ['.xlsx', '.csv']

        if extension not in valid_extensions:
            raise ValidationError('File type not supported')
        return data
