import json
import os
from django.conf import settings
from django.contrib.auth.models import User
from django.core.management import BaseCommand
from mainapp.models import Product, ProductCategory
from authapp.models import ShopUser


def load_from_json(file_name):
    with open(os.path.join(settings.BASE_DIR, f'mainapp/json/{file_name}.json')) as f:
        return json.load(f)


class Command(BaseCommand):

    def handle(self, *arg, **option):
        categories = load_from_json('categories')

        ProductCategory.objects.all().delete()
        for cat in categories:
            ProductCategory.objects.create(**cat)

        products = load_from_json('products')

        Product.objects.all().delete()
        for product in products:
            # Получаем категорию по имени
            _category = ProductCategory.objects.get(name=product["category"])
            # Заменяем название категории объектом
            product['category'] = _category
            Product.objects.create(**product)

        ShopUser.objects.create_superuser('django', 'zh@li.ru', 'geekbrains', age=30)