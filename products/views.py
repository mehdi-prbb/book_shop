from django.views import generic

from .models import Mobile


class MobileListView(generic.ListView):
    queryset = Mobile.objects.select_related('product').prefetch_related('mobile_colors')
    template_name = 'products/mobile_list.html'
    context_object_name = 'mobiles'