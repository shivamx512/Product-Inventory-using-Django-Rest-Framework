from django.core.management.base import BaseCommand
from faker import Faker
import random

from product_inventory.models import Product, ProductCategory


class Command(BaseCommand):
    help = 'Populate 1000 products data in the database using faker library'

    def handle(self, *args, **kwargs):
        product_category = []
        categories = [
            "smartphone",
            "laptop",
            "computer",
            "printer",
            "earphone",
            "headphone",
            "speaker",
            "charger",
        ]
        if ProductCategory.objects.count() == 0:
            for category in categories:
                product_category.append(ProductCategory(name=category))

            ProductCategory.objects.bulk_create(product_category)
        categories = list(ProductCategory.objects.all())

        if Product.objects.count() == 0:
            faker = Faker()
            products = []

            for _ in range(1000):
                name = faker.word()
                category = random.choice(categories)
                price = round(random.uniform(1.00, 1000.00), 2)
                products.append(Product(name=name, category=category, price=price))
            # bulk create for single db query
            Product.objects.bulk_create(products)
            self.stdout.write(self.style.SUCCESS('Successfully created 1000 products'))
        else:
            self.stdout.write(self.style.SUCCESS('Products already exists'))
