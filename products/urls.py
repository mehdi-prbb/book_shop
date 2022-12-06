from django.urls import path, re_path

from .views import MobileListView, LaptopListView, AllProductsListView, MobileDetailView, LaptopDetailView


urlpatterns = [
    path('', AllProductsListView.as_view(), name='all_products'),
    path('laptop/', LaptopListView.as_view(), name='laptop_list'),
    path('mobile/', MobileListView.as_view(), name='mobile_list'),
    re_path(r'laptop/(?P<laptop_slug>[-\w]+)/', LaptopDetailView.as_view(), name='laptop_detail'),
    re_path(r'mobile/(?P<mobile_slug>[-\w]+)/', MobileDetailView.as_view(), name='mobile_detail'),
]
