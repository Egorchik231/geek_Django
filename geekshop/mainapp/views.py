from datetime import datetime

from django.shortcuts import render


def main(request):
    context = {
        'title': 'Главная',
        'date': datetime.now()
    }
    return render(request, 'mainapp/index.html', context)


def products(request):
    links_menu = [
        {'href': 'products_all', 'name': 'все'},
        {'href': 'products_home', 'name': 'дом'},
        {'href': 'products_office', 'name': 'офис'},
        {'href': 'products_modern', 'name': 'модерн'},
        {'href': 'products_classic', 'name': 'классика'},
    ]
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
