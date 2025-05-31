from django import forms
from datetime import date

YEAR_CHOICES = [(y, y) for y in range(2022, date.today().year + 1)]


class StatsFilterForm(forms.Form):
    year = forms.ChoiceField(
        choices=YEAR_CHOICES,
        required=True,
        widget=forms.Select(attrs={"class": "form-select"}),
    )
