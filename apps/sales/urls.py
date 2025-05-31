from django.urls import path
from . import views

urlpatterns = [
    path("customers/", views.CustomerList.as_view(), name="customer_list"),
    path("customers/new/", views.CustomerCreate.as_view(), name="customer_create"),
    path(
        "customers/<int:pk>/edit/",
        views.CustomerUpdate.as_view(),
        name="customer_update",
    ),
    path(
        "customers/<int:pk>/del/",
        views.CustomerDelete.as_view(),
        name="customer_delete",
    ),
    path("", views.SaleOrderList.as_view(), name="sale_list"),
    path("new/", views.SaleOrderCreate.as_view(), name="sale_create"),
    path("<int:pk>/", views.SaleOrderDetail.as_view(), name="sale_detail"),
    path("orders/<int:pk>/edit/", views.SaleOrderUpdate.as_view(), name="sale_update"),
]
