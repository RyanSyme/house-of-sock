from django.shortcuts import render, reverse
from django.urls import path
from products.views import Product

import random


def index(request):
    """
        View returns index page
    """
    products = Product.objects.all()

    products_slider = random.sample(
        list(products), 6)

    context = {
        'products_slider': products_slider
    }

    return render(request, 'home/index.html', context)
