from django import forms
from django.conf import settings


class GameForm(forms.Form):
    value = forms.IntegerField(min_value=settings.GAME_MIN_VALUE,
                               max_value=settings.GAME_MAX_VALUE,
                               label='Введите число')
