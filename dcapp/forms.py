from dataclasses import fields
from django import forms
from dcapp.models import DCModel

class DCForm(forms.ModelForm):
    class Meta:
        model=DCModel
        fields="__all__"