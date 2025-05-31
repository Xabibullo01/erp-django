from django.urls import reverse_lazy
from django.views import generic
from django.utils.decorators import method_decorator
from apps.inventory.models import Product, Category, Warehouse
from apps.inventory.forms import ProductForm, CategoryForm, WarehouseForm
from apps.users.decorators import role_required


@method_decorator(role_required("ADMIN", "SUPERADMIN"), name="dispatch")
class ProductList(generic.ListView):
    model = Product
    template_name = "inventory/product_list.html"


@method_decorator(role_required("ADMIN", "SUPERADMIN"), name="dispatch")
class ProductCreate(generic.CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("product_list")
    template_name = "inventory/product_form.html"


@method_decorator(role_required("ADMIN", "SUPERADMIN"), name="dispatch")
class ProductUpdate(generic.UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("product_list")
    template_name = "inventory/product_form.html"


@method_decorator(role_required("ADMIN", "SUPERADMIN"), name="dispatch")
class ProductDelete(generic.DeleteView):
    model = Product
    success_url = reverse_lazy("product_list")
    template_name = "partials/confirm_delete.html"


@method_decorator(role_required("ADMIN", "SUPERADMIN"), name="dispatch")
class CategoryList(generic.ListView):
    model = Category
    template_name = "inventory/category_list.html"


@method_decorator(role_required("ADMIN", "SUPERADMIN"), name="dispatch")
class CategoryCreate(generic.CreateView):
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy("inv_category_list")
    template_name = "inventory/category_form.html"


@method_decorator(role_required("ADMIN", "SUPERADMIN"), name="dispatch")
class CategoryUpdate(generic.UpdateView):
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy("inv_category_list")
    template_name = "inventory/category_form.html"


@method_decorator(role_required("ADMIN", "SUPERADMIN"), name="dispatch")
class CategoryDelete(generic.DeleteView):
    model = Category
    success_url = reverse_lazy("inv_category_list")
    template_name = "partials/confirm_delete.html"


# ======== WAREHOUSE ========
@method_decorator(role_required("ADMIN", "SUPERADMIN"), name="dispatch")
class WarehouseList(generic.ListView):
    model = Warehouse
    template_name = "inventory/warehouse_list.html"


@method_decorator(role_required("ADMIN", "SUPERADMIN"), name="dispatch")
class WarehouseCreate(generic.CreateView):
    model = Warehouse
    form_class = WarehouseForm
    success_url = reverse_lazy("warehouse_list")
    template_name = "inventory/warehouse_form.html"


@method_decorator(role_required("ADMIN", "SUPERADMIN"), name="dispatch")
class WarehouseUpdate(generic.UpdateView):
    model = Warehouse
    form_class = WarehouseForm
    success_url = reverse_lazy("warehouse_list")
    template_name = "inventory/warehouse_form.html"


@method_decorator(role_required("ADMIN", "SUPERADMIN"), name="dispatch")
class WarehouseDelete(generic.DeleteView):
    model = Warehouse
    success_url = reverse_lazy("warehouse_list")
    template_name = "partials/confirm_delete.html"
