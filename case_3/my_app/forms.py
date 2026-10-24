from django import forms
from .models import Name

class NameForm(forms.ModelForm):
    class Meta:
        model = Name
        fields = ['name']
        labels = {'name': 'Введите ваше имя'}