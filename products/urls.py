from django.urls import path

from .views import MobileListView, LaptopListView, AllProductsListView


urlpatterns = [
    path('', AllProductsListView.as_view(), name='all_products'),
    path('mobile/', MobileListView.as_view(), name='mobile_list'),
    path('laptop/', LaptopListView.as_view(), name='laptop_list'),
]
