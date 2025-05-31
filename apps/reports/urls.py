from django.urls import path
from . import views

urlpatterns = [
    path("sales/csv/", views.sales_csv, name="report_sales_csv"),
]
