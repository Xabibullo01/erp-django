from django import forms
from .models import Supplier, PurchaseOrder, PurchaseOrderLine


class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ["name", "phone", "address"]
        widgets = {f: forms.TextInput(attrs={"class": "form-control"}) for f in fields}


class PurchaseOrderForm(forms.ModelForm):
    class Meta:
        model = PurchaseOrder
        fields = ["supplier", "warehouse", "note"]
        widgets = {
            "supplier": forms.Select(attrs={"class": "form-select"}),
            "warehouse": forms.Select(attrs={"class": "form-select"}),
            "note": forms.TextInput(attrs={"class": "form-control"}),
        }


class PurchaseOrderLineForm(forms.ModelForm):
    class Meta:
        model = PurchaseOrderLine
        fields = ["product", "quantity", "cost"]
        widgets = {
            "product": forms.Select(attrs={"class": "form-select"}),
            "quantity": forms.NumberInput(attrs={"class": "form-control"}),
            "cost": forms.NumberInput(attrs={"class": "form-control"}),
        }
