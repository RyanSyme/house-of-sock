from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There's nothing in the cart just yet")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51IOOX2IxSQF4HiQYpN3KX3mtBmo1lFESmXI6rQ1bns3JsAxAB4GemfO01YVTZxR9ZJqvIwjMNsyFGUIYlbzGpkyE00Oi4MlVGD',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
