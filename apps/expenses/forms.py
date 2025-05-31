from django import forms
from .models import ExpenseCategory, Expense


class ExpenseCategoryForm(forms.ModelForm):
    class Meta:
        model = ExpenseCategory
        fields = ["name"]
        widgets = {"name": forms.TextInput(attrs={"class": "form-control"})}


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ["category", "amount", "note"]
        widgets = {
            "category": forms.Select(attrs={"class": "form-select"}),
            "amount": forms.NumberInput(attrs={"class": "form-control"}),
            "note": forms.TextInput(attrs={"class": "form-control"}),
        }
