from django.db import models
from apps.core.models import TimeStampedMixin
from apps.inventory.models import Product, Warehouse


class Supplier(TimeStampedMixin):
    name = models.CharField(max_length=120)
    phone = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name


class PurchaseOrder(TimeStampedMixin):
    supplier = models.ForeignKey(Supplier, on_delete=models.PROTECT)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.PROTECT)
    note = models.CharField(max_length=255, blank=True)

    @property
    def total(self):
        return sum(line.subtotal for line in self.lines.all())

    def __str__(self):
        return f"PO-{self.pk}"


class PurchaseOrderLine(models.Model):
    order = models.ForeignKey(
        PurchaseOrder, related_name="lines", on_delete=models.CASCADE
    )
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()
    cost = models.DecimalField(max_digits=12, decimal_places=2)

    @property
    def subtotal(self):
        return self.quantity * self.cost
