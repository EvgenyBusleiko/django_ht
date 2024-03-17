import datetime

from django import forms
from django.db import models


class DiceForm(forms.Form):
    METHOD_CHOICES = (('Coin', 'Монета'), ('Dice', 'Кубик'), ('Hundred', 'Случайное число до 100'))
    method = forms.ChoiceField(choices=METHOD_CHOICES)
    count = forms.IntegerField(max_value=100)
