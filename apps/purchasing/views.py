from django.forms import inlineformset_factory
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View, generic

from apps.inventory.models import Product
from apps.purchasing.models import Supplier, PurchaseOrder, PurchaseOrderLine
from apps.purchasing.forms import (
    SupplierForm,
    PurchaseOrderForm,
    PurchaseOrderLineForm,
)
from apps.users.decorators import role_required

admin_only = method_decorator(role_required("ADMIN", "SUPERADMIN"), name="dispatch")

PurchaseLineFormSet = inlineformset_factory(
    PurchaseOrder,
    PurchaseOrderLine,
    form=PurchaseOrderLineForm,
    extra=1,
    can_delete=True,
)


@admin_only
class SupplierList(generic.ListView):
    model = Supplier
    template_name = "purchasing/supplier_list.html"


@admin_only
class SupplierCreate(generic.CreateView):
    model = Supplier
    form_class = SupplierForm
    template_name = "purchasing/supplier_form.html"
    success_url = reverse_lazy("supplier_list")


@admin_only
class SupplierUpdate(generic.UpdateView):
    model = Supplier
    form_class = SupplierForm
    template_name = "purchasing/supplier_form.html"
    success_url = reverse_lazy("supplier_list")


@admin_only
class SupplierDelete(generic.DeleteView):
    model = Supplier
    template_name = "partials/confirm_delete.html"
    success_url = reverse_lazy("supplier_list")


@admin_only
class PurchaseList(generic.ListView):
    model = PurchaseOrder
    ordering = "-created_at"
    template_name = "purchasing/purchase_list.html"


@admin_only
class PurchaseCreate(View):
    template_name = "purchasing/purchase_form.html"

    def get(self, request):
        order_form = PurchaseOrderForm()
        formset = PurchaseLineFormSet()
        return render(
            request,
            self.template_name,
            {
                "form": order_form,
                "formset": formset,
                "products": Product.objects.all(),
            },
        )

    def post(self, request):
        order_form = PurchaseOrderForm(request.POST)
        formset = PurchaseLineFormSet(request.POST)

        if order_form.is_valid() and formset.is_valid():
            order = order_form.save()
            formset.instance = order
            formset.save()
            return redirect("purchase_list")

        return render(
            request,
            self.template_name,
            {
                "form": order_form,
                "formset": formset,
                "products": Product.objects.all(),
            },
        )


@admin_only
class PurchaseUpdate(View):
    template_name = "purchasing/purchase_form.html"

    def get(self, request, pk):
        order = get_object_or_404(PurchaseOrder, pk=pk)
        order_form = PurchaseOrderForm(instance=order)
        formset = PurchaseLineFormSet(instance=order)
        return render(
            request,
            self.template_name,
            {
                "form": order_form,
                "formset": formset,
                "products": Product.objects.all(),
                "object": order,
            },
        )

    def post(self, request, pk):
        order = get_object_or_404(PurchaseOrder, pk=pk)
        order_form = PurchaseOrderForm(request.POST, instance=order)
        formset = PurchaseLineFormSet(request.POST, instance=order)

        if order_form.is_valid() and formset.is_valid():
            order_form.save()
            formset.save()
            return redirect("purchase_list")

        return render(
            request,
            self.template_name,
            {
                "form": order_form,
                "formset": formset,
                "products": Product.objects.all(),
                "object": order,
            },
        )
