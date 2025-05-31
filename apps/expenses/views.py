from django.urls import reverse_lazy
from django.views import generic
from django.utils.decorators import method_decorator

from apps.expenses.models import ExpenseCategory, Expense
from apps.expenses.forms import ExpenseCategoryForm, ExpenseForm
from apps.users.decorators import role_required


admin_only = method_decorator(role_required("ADMIN", "SUPERADMIN"), name="dispatch")


@admin_only
class ExpenseCategoryList(generic.ListView):
    model = ExpenseCategory
    template_name = "expenses/category_list.html"


@admin_only
class ExpenseCategoryCreate(generic.CreateView):
    model = ExpenseCategory
    form_class = ExpenseCategoryForm
    success_url = reverse_lazy("exp_cat_list")
    template_name = "expenses/category_form.html"


@admin_only
class ExpenseCategoryUpdate(generic.UpdateView):
    model = ExpenseCategory
    form_class = ExpenseCategoryForm
    success_url = reverse_lazy("exp_cat_list")
    template_name = "expenses/category_form.html"


@admin_only
class ExpenseCategoryDelete(generic.DeleteView):
    model = ExpenseCategory
    success_url = reverse_lazy("exp_cat_list")
    template_name = "partials/confirm_delete.html"


@admin_only
class ExpenseList(generic.ListView):
    model = Expense
    template_name = "expenses/expense_list.html"


@admin_only
class ExpenseCreate(generic.CreateView):
    model = Expense
    form_class = ExpenseForm
    success_url = reverse_lazy("expense_list")
    template_name = "expenses/expense_form.html"
