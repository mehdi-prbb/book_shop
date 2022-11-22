from django.views import generic

from .models import Mobile, Laptop


class MobileListView(generic.ListView):
    queryset = Mobile.objects.select_related('product').prefetch_related('choices')
    template_name = 'products/mobile_list.html'
    context_object_name = 'mobiles'


class LaptopListView(generic.ListView):
    queryset = Laptop.objects.select_related('product').prefetch_related('choices')
    template_name = 'products/laptop_list.html'
    context_object_name = 'laptops'
