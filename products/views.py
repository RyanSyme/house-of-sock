from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.http import HttpResponseRedirect

from .models import Product, Category, Review
from .forms import ProductForm


def all_products(request):
    """
        View returns all products page
    """
    products = Product.objects.all()

    query = None
    categories = None
    # args = request.GET.items()
    # print("args", args)

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(",")
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        # search function
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "No search criteria entered!!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(
                description__icontains=query)
            products = products.filter(queries)

    # Pagination
    paginator = Paginator(products, 12)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'page_obj': page_obj
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """
        View returns details of single product
    """

    product = get_object_or_404(Product, pk=product_id)

    # Add review
    if request.method == 'POST' and request.user.is_authenticated:
        stars = request.POST.get('stars', '5')
        content = request.POST.get('content', '')

        review = Review.objects.create(product=product, user=request.user,
                                       stars=stars, content=content)

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    context = {
        'product': product
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """
        Gives admin ability to add products to the store
    """
    if not request.user.is_superuser:
        messages.error(request,
                       'Sorry, only admin can add products to the store')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added a product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. \
                Please check to ensure the form is valid')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """
        Gives admin ability to edit products to the store
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only admin can edit products')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product successfuly updated!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. \
                Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """
        view to delete product from store
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, \
            only admin can remove products from the store')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))
