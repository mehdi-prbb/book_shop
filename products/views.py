from django.views import generic

from .models import Mobile, Laptop, Product
from cart.forms import AddToCartForm


class AllProductsListView(generic.ListView):
    queryset = Product.objects.all().select_related('mobiles', 'laptops')
    template_name = 'products/all_products.html'
    context_object_name = 'products'


class MobileListView(generic.ListView):
    queryset = Mobile.objects.select_related('product').prefetch_related('choices')
    template_name = 'products/mobile_list.html'
    context_object_name = 'mobiles'


class MobileDetailView(generic.DetailView):
    model = Mobile
    template_name = 'products/mobile_details.html'
    slug_field = 'product__slug'
    slug_url_kwarg = 'mobile_slug'
    

class LaptopListView(generic.ListView):
    queryset = Laptop.objects.select_related('product').prefetch_related('choices')
    template_name = 'products/laptop_list.html'
    context_object_name = 'laptops'


class LaptopDetailView(generic.DetailView):
    model = Laptop
    template_name = 'products/laptop_details.html'
    slug_field = 'product__slug'
    slug_url_kwarg = 'laptop_slug'

