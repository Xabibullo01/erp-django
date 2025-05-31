from django.db import transaction
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View, generic

from apps.inventory.models import Product
from apps.users.decorators import role_required
from .models import Customer, SaleOrder
from .forms import CustomerForm, SaleOrderForm, SaleLineFormSet


admin_only = method_decorator(role_required("ADMIN", "SUPERADMIN"), name="dispatch")
admin_and_staff = method_decorator(
    role_required("ADMIN", "SUPERADMIN", "STAFF"), name="dispatch"
)


@admin_only
class CustomerList(generic.ListView):
    model = Customer
    template_name = "sales/customer_list.html"


@admin_only
class CustomerCreate(generic.CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = "sales/customer_form.html"
    success_url = reverse_lazy("customer_list")


@admin_only
class CustomerUpdate(generic.UpdateView):
    model = Customer
    form_class = CustomerForm
    template_name = "sales/customer_form.html"
    success_url = reverse_lazy("customer_list")


@admin_only
class CustomerDelete(generic.DeleteView):
    model = Customer
    template_name = "partials/confirm_delete.html"
    success_url = reverse_lazy("customer_list")


@admin_and_staff
class SaleOrderList(generic.ListView):
    model = SaleOrder
    template_name = "sales/saleorder_list.html"


@admin_and_staff
class SaleOrderDetail(generic.DetailView):
    model = SaleOrder
    template_name = "sales/saleorder_detail.html"


class _SaleOrderMixin(View):

    template_name = "sales/saleorder_form.html"
    form_prefix = "lines"  # formset prefix

    def _ctx(self, order_form, formset, **extra):

        ctx = {
            "form": order_form,
            "formset": formset,
            "products": Product.objects.all(),
        }
        ctx.update(extra)
        return ctx

    def _bind_formset(self, *args, **kwargs):
        return SaleLineFormSet(*args, prefix=self.form_prefix, **kwargs)

    def _apply_prices(self, formset):
        for form in formset:
            if form.cleaned_data.get("product") and not form.cleaned_data.get("DELETE"):
                form.instance.price = form.cleaned_data["product"].sell_price


@admin_and_staff
class SaleOrderCreate(_SaleOrderMixin):

    def get(self, request):
        return render(
            request,
            self.template_name,
            self._ctx(SaleOrderForm(), self._bind_formset()),
        )

    @transaction.atomic
    def post(self, request):
        order_form = SaleOrderForm(request.POST)
        formset = self._bind_formset(request.POST)

        if order_form.is_valid() and formset.is_valid():
            order = order_form.save(commit=False)
            order.cashier = request.user
            order.save()

            self._apply_prices(formset)
            formset.instance = order
            formset.save()
            return redirect("sale_detail", pk=order.pk)

        return render(request, self.template_name, self._ctx(order_form, formset))


@admin_and_staff
class SaleOrderUpdate(_SaleOrderMixin):

    def get(self, request, pk):
        order = get_object_or_404(SaleOrder, pk=pk)
        order_f = SaleOrderForm(instance=order)
        formset_f = self._bind_formset(instance=order)
        return render(
            request, self.template_name, self._ctx(order_f, formset_f, object=order)
        )

    @transaction.atomic
    def post(self, request, pk):
        order = get_object_or_404(SaleOrder, pk=pk)
        order_f = SaleOrderForm(request.POST, instance=order)
        formset_f = self._bind_formset(request.POST, instance=order)

        if order_f.is_valid() and formset_f.is_valid():
            order_f.save()

            self._apply_prices(formset_f)
            formset_f.save()
            return redirect("sale_detail", pk=order.pk)

        return render(
            request, self.template_name, self._ctx(order_f, formset_f, object=order)
        )
