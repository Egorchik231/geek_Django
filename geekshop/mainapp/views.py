from datetime import datetime
from django.shortcuts import render
from mainapp.models import Product, ProductCategory


def main(request):

    products = Product.objects.all()
    context = {
        'title': 'Главная',
        'date': datetime.now(),
        'products': products[:4]
    }
    return render(request, 'mainapp/index.html', context)


def products(request, pk=None):
    links_menu = ProductCategory.objects.all()
    context = {
        'title': 'Товары',
        'date': datetime.now(),
        'links_menu': links_menu
    }
    return render(request, 'mainapp/products.html', context)


def contact(request):
    context = {
        'title': 'Контакты',
        'date': datetime.now()
    }
    return render(request, 'mainapp/contact.html', context)

# Create your templates here.
