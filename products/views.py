from django.shortcuts import render
from .models import Product


def all_products(request):
    """
        View returns all products page
    """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)
