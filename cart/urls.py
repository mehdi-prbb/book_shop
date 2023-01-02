from django.urls import path, re_path

from .views import cart_detail_view, add_to_cart_view, remove_from_cart, clear_cart

app_name = 'cart'

urlpatterns = [
    path('', cart_detail_view, name='cart_detail'),
    re_path(r'add/(?P<product_slug>[-\w]+)/', add_to_cart_view, name='add_to_cart'),
    re_path(r'remove/(?P<product_slug>[-\w]+)/', remove_from_cart, name='remove_cart'),
    path('clear/', clear_cart, name='cart_clear')
]
