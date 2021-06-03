from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404)
from django.contrib import messages
from products.models import Product


def view_cart(request):
    """
        View returns shopping cart contents page
    """
    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """
        Adds specified product to the cart
    """
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    cart = request.session.get('cart', {})

    if size:
        if item_id in list(cart.keys()):
            if size in cart[item_id]['items_by_size'].keys():
                cart[item_id]['items_by_size'][size] += quantity
                messages.success(request,
                                 (f'Added a Size {size.upper()} '
                                  f'{product.name}, Total Qty '
                                  f'{cart[item_id]["items_by_size"][size]}'))
            else:
                cart[item_id]['items_by_size'][size] = quantity
                messages.success(request,
                                 (f'Added a Size {size.upper()} '
                                  f'{product.name} to the cart'))
        else:
            cart[item_id] = {'items_by_size': {size: quantity}}
            messages.success(request,
                             (f'Added a Size {size.upper()} '
                              f'{product.name} to the cart'))
    else:
        if item_id in list(cart.keys()):
            cart[item_id] += quantity
            messages.success(request,
                             (f'Added {product.name} '
                              f'to {cart[item_id]}'))
        else:
            cart[item_id] = quantity
            messages.success(request, f'Added {product.name} to the cart')

    request.session['cart'] = cart
    return redirect(redirect_url)


def adjust_cart(request, item_id):
    """
        Adjusts product quantities in the cart
    """
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    cart = request.session.get('cart', {})

    if size:
        if quantity > 0:
            cart[item_id]['items_by_size'][size] = quantity
            messages.success(
                request, f'Updated Size {size.upper()} {product.name} quantity to {cart[item_id]["items_by_size"][size]}')
        else:
            del cart[item_id]['items_by_size'][size]
            if not cart[item_id]['items_by_size']:
                cart.pop(item_id)
            messages.success(
                request, f'Removed Size {size.upper()} {product.name} from the cart')
    else:
        if quantity > 0:
            cart[item_id] = quantity
            messages.success(
                request, f'Updated {product.name} quantity to {cart[item_id]}')
        else:
            cart.pop(item_id)
            messages.success(request, f'Removed {product.name} from the cart')

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, item_id):
    """
        Remove specified item from cart
    """
    try:
        product = get_object_or_404(Product, pk=item_id)
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        cart = request.session.get('cart', {})

        if size:
            del cart[item_id]['items_by_size'][size]
            if not cart[item_id]['items_by_size']:
                cart.pop(item_id)
            messages.success(request, f'Removed size {size.upper()}\
                 {product.name} from the cart')
        else:
            cart.pop(item_id)
            messages.success(request, f'Removed {product.name} from the cart')

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
