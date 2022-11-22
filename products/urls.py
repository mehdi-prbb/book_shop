from django.urls import path

from .views import MobileListView, LaptopListView


urlpatterns = [
    path('mobile/', MobileListView.as_view(), name='mobile_list'),
    path('laptop/', LaptopListView.as_view(), name='laptop_list'),
]
