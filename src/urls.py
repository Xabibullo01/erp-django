from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),

    # Auth
    path("login/", LoginView.as_view(template_name="auth/login.html"), name="login"),
    path("logout/", LogoutView.as_view(next_page="login"), name="logout"),
    # Modules
    path("", include("apps.dashboard.urls")),
    path("users/", include("apps.users.urls")),
    path("inventory/", include("apps.inventory.urls")),
    path("sales/", include("apps.sales.urls")),
    path("purchasing/", include("apps.purchasing.urls")),
    path("expenses/", include("apps.expenses.urls")),
    path("reports/", include("apps.reports.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
