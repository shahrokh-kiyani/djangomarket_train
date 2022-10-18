from django.views import generic
from django.shortcuts import get_object_or_404, render

from .models import Product, Comment
from .forms import CommentForm


class ProductListView(generic.ListView):
    queryset = Product.objects.filter(status=True)
    template_name = 'products/product_list.html'
    context_object_name = 'products'


def detail_view(request, slug):
    product = get_object_or_404(Product, slug=slug, status=True)
    comments = product.comments.filter(active=True)

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)

        new_comment = comment_form.save(commit=False)
        new_comment.author = request.user
        new_comment.product = product
        new_comment.save()

    else:
        comment_form = CommentForm

    context = {
        'product': product,
        'comment': comments,
        'form': comment_form,
    }

    return render(request, 'products/product_detail.html', context)
