from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from faker import Faker
from random import randint, choice, uniform
from decimal import Decimal

from apps.inventory.models import Category, Product, Warehouse, StockMovement
from apps.sales.models import Customer, SaleOrder, SaleOrderLine
from apps.purchasing.models import Supplier, PurchaseOrder, PurchaseOrderLine
from apps.expenses.models import ExpenseCategory, Expense

fake = Faker("uz_UZ")
User = get_user_model()


class Command(BaseCommand):
    help = "Demo ma'lumotlarni Faker yordamida yaratadi"

    def add_arguments(self, parser):
        parser.add_argument(
            "--scale",
            type=int,
            default=30,
            help="Har bir modelga taxminan nechta obyekt yaratiladi (default 30)",
        )

    def handle(self, *args, **opts):
        scale = opts["scale"]
        self.stdout.write(self.style.NOTICE(f"↺  Demo ma'lumotlar ({scale=}):"))

        # --- 1) Kategoriya, Omborxona, Supplier & h.k. ---
        # Kategoriya: unique nomlar
        cat_names = set(Category.objects.values_list("name", flat=True))
        while len(cat_names) < scale:
            cat_names.add(fake.unique.word())

        cats = []
        for name in list(cat_names)[-scale:]:
            obj, _ = Category.objects.get_or_create(name=name)
            cats.append(obj)

        # Omborxona
        wh_names = set(Warehouse.objects.values_list("name", flat=True))
        while len(wh_names) < 5:
            wh_names.add(fake.unique.company())

        whs = []
        for name in list(wh_names)[-5:]:
            obj, _ = Warehouse.objects.get_or_create(name=name)
            whs.append(obj)

        # Supplier
        sup_names = set(Supplier.objects.values_list("name", flat=True))
        while len(sup_names) < scale:
            sup_names.add(fake.unique.company())

        sups = []
        for name in list(sup_names)[-scale:]:
            obj, _ = Supplier.objects.get_or_create(
                name=name,
                defaults={
                    "phone": fake.phone_number(),
                    "address": fake.address(),
                },
            )
            sups.append(obj)

        # --- 2) Mahsulotlar ---
        products = []
        for _ in range(scale * 3):
            name = fake.unique.word().capitalize()
            sku = fake.unique.bothify(text="???-#####")
            category = choice(cats)
            cost_price = Decimal(randint(1000, 9000))
            sell_price = Decimal(randint(11000, 50000))
            size = str(choice([42, 44, 46, "L", "XL"]))
            color = fake.color_name()
            product, _ = Product.objects.get_or_create(
                sku=sku,
                defaults={
                    "name": name,
                    "category": category,
                    "cost_price": cost_price,
                    "sell_price": sell_price,
                    "size": size,
                    "color": color,
                },
            )
            products.append(product)

            # Boshlang‘ich zaxira
            StockMovement.objects.create(
                product=product,
                warehouse=choice(whs),
                movement_type=StockMovement.Type.IN,
                quantity=randint(20, 100),
            )

        # --- 3) Mijozlar ---
        customers = []
        for _ in range(scale):
            first_name = fake.first_name()
            last_name = fake.last_name()
            phone = fake.phone_number()
            address = fake.address()
            customer, _ = Customer.objects.get_or_create(
                first_name=first_name,
                last_name=last_name,
                phone=phone,
                defaults={"address": address},
            )
            customers.append(customer)

        # --- 4) Sotuv buyurtmalari ---
        for _ in range(scale * 2):
            so = SaleOrder.objects.create(
                customer=choice(customers),
                cashier=User.objects.first(),
                note=fake.text(max_nb_chars=20),
            )
            for _ in range(randint(1, 5)):
                prod = choice(products)
                qty = randint(1, 5)
                SaleOrderLine.objects.create(
                    order=so, product=prod, quantity=qty, price=prod.sell_price
                )
                # Ombordan chiqim
                StockMovement.objects.create(
                    product=prod,
                    warehouse=choice(whs),
                    movement_type=StockMovement.Type.OUT,
                    quantity=qty,
                )

        # --- 5) Xarid buyurtmalari ---
        for _ in range(scale):
            po = PurchaseOrder.objects.create(
                supplier=choice(sups), warehouse=choice(whs), note=fake.word()
            )
            for _ in range(randint(1, 4)):
                prod = choice(products)
                qty = randint(10, 50)
                cost = prod.cost_price + Decimal(randint(500, 3000))
                PurchaseOrderLine.objects.create(
                    order=po, product=prod, quantity=qty, cost=cost
                )
                # Omborga kirim
                StockMovement.objects.create(
                    product=prod,
                    warehouse=po.warehouse,
                    movement_type=StockMovement.Type.IN,
                    quantity=qty,
                )

        # --- 6) Harajat kategoriyalari & harajatlar ---
        exp_cat_names = set(ExpenseCategory.objects.values_list("name", flat=True))
        while len(exp_cat_names) < 6:
            exp_cat_names.add(fake.unique.word())

        exp_cats = []
        for name in list(exp_cat_names)[-6:]:
            obj, _ = ExpenseCategory.objects.get_or_create(name=name)
            exp_cats.append(obj)

        for _ in range(scale * 3):
            Expense.objects.create(
                category=choice(exp_cats),
                amount=Decimal(uniform(5_000, 200_000)).quantize(Decimal("0.01")),
                note=fake.sentence(nb_words=3),
                user=User.objects.first(),
            )

        self.stdout.write(self.style.SUCCESS("✓  Demo ma'lumotlar tayyor!"))
