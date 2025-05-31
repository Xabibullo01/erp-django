import csv
from django.http import HttpResponse
from django.contrib.auth.decorators import user_passes_test
from django.utils import timezone
from apps.sales.models import SaleOrderLine

admin_required = user_passes_test(lambda u: u.is_superuser or u.role == "ADMIN")


@admin_required
def sales_csv(request):
    today = timezone.now().strftime("%Y%m%d")
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = f'attachment; filename="sales_{today}.csv"'

    writer = csv.writer(response)
    writer.writerow(["Date", "Product", "Qty", "Price", "Subtotal"])

    lines = SaleOrderLine.objects.select_related("order", "product").order_by(
        "-order__created_at"
    )[:5000]
    for line in lines:
        writer.writerow(
            [
                line.order.created_at.strftime("%Y-%m-%d"),
                line.product.name,
                line.quantity,
                line.price,
                line.subtotal,
            ]
        )
    return response
