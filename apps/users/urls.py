from django.urls import path
from .views import UserList, UserCreate, UserUpdate, UserDelete

urlpatterns = [
    path("", UserList.as_view(), name="user_list"),
    path("new/", UserCreate.as_view(), name="user_create"),
    path("<int:pk>/edit/", UserUpdate.as_view(), name="user_update"),
    path("<int:pk>/delete/", UserDelete.as_view(), name="user_delete"),
]
