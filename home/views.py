from django.shortcuts import render
from django.urls import path
from products.models import Category, Product

import random


def index(request):
    """
        View returns index page
    """
    category = Category.objects.all()
    products_slider = Product.objects.all().order_by('-id')[:6]

    page='home'
    context={
        'page': page,
        'products_slider': products_slider,
        'category': category
    }

    return render(request, 'home/index.html', context)
