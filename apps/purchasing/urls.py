from django.urls import path
from . import views

urlpatterns = [
    path("suppliers/", views.SupplierList.as_view(), name="supplier_list"),
    path("suppliers/new/", views.SupplierCreate.as_view(), name="supplier_create"),
    path(
        "suppliers/<int:pk>/edit/",
        views.SupplierUpdate.as_view(),
        name="supplier_update",
    ),
    path(
        "suppliers/<int:pk>/del/",
        views.SupplierDelete.as_view(),
        name="supplier_delete",
    ),
    path("", views.PurchaseList.as_view(), name="purchase_list"),
    path("new/", views.PurchaseCreate.as_view(), name="purchase_create"),
]
