from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from django.http import HttpResponseRedirect
from django.contrib import messages


from products.models import Product
from .cart import Cart
from .forms import AddToCartForm


def cart_detail_view(request):
    cart = Cart(request)

    for item in cart:
        item['quantity_update_form'] = AddToCartForm(initial={
            'quantity' : item['quantity'],
            'inplace' : True,
        })

    return render(request, 'cart/cart_detail.html', {'cart' : cart})


@require_POST
def add_to_cart_view(request, product_slug):
    cart = Cart(request)

    product = get_object_or_404(Product, slug=product_slug)
    form = AddToCartForm(request.POST)

    if form.is_valid():
        cleaned_data = form.cleaned_data
        quantity = cleaned_data['quantity']
        cart.add(product, quantity, replace_current_quantity=cleaned_data['inplace'])

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def remove_from_cart(request, product_slug):
    cart = Cart(request)

    product = get_object_or_404(Product, slug=product_slug)

    cart.remove(product)

    return redirect('cart:cart_detail')


@require_POST
def clear_cart(request):
    cart = Cart(request)

    if len(cart):
        cart.clear()
        messages.success(request, 'your cart successfully cleared.')
    else:
        messages.warning(request, 'your cart already empty.')

    return redirect('cart:cart_detail')