from django.urls import path

from .views import MobileListView


urlpatterns = [
    path('mobile/', MobileListView.as_view(), name='products_list'),
]
