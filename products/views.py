from django.views import generic
from django.shortcuts import get_object_or_404

from .models import Product
from .forms import CommnetForm


class ProductListView(generic.ListView):
    queryset = Product.objects.filter(status=True)
    template_name = 'products/product_list.html'
    context_object_name = 'products'


class ProductDetailView(generic.DetailView):
    queryset = Product.objects.all()
    template_name = 'products/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommnetForm()
        return context
