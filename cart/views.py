from django.shortcuts import render


def view_cart(request):
    """
        View returns shopping cart contents page
    """
    return render(request, 'cart/cart.html')
