from django.shortcuts import render
from django.urls import path
from products.models import Category, Product


def index(request):
    """
        View returns index page
    """
    category = Category.objects.all()
    products_latest = Product.objects.all().order_by('-id')[:4]

    page = 'home'
    context = {
        'page': page,
        'products_latest': products_latest,
        'category': category
    }

    return render(request, 'home/index.html', context)
