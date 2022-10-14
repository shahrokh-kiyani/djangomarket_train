from django.views import generic
from django.shortcuts import get_object_or_404

from .models import Product


class ProductListView(generic.ListView):
    queryset = Product.objects.filter(status=True)
    template_name = 'products/product_list.html'
    context_object_name = 'products'


class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'
